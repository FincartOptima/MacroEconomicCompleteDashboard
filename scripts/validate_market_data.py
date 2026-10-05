"""Validate the four reviewed series and reproduce monthly NSE P/E averages."""
import json
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'data.json').read_text())['indicators']
inputs = json.loads((ROOT / 'data/nifty50-pe-daily.json').read_text())
months = {f'{y}-{m:02}' for y in (2024, 2025, 2026) for m in range(1, 13)
          if '2024-10' <= f'{y}-{m:02}' <= '2026-09'}
keys = ('t_bill_91d_yield', 't_bill_364d_yield', 'ten_year_gsec_yield', 'nifty50_pe')
for key in keys:
    assert months <= data[key].keys(), f'Missing reviewed months: {key}'
    for month in months:
        entry = data[key][month]
        field = 'pe_ratio' if key == 'nifty50_pe' else 'yield_pct'
        assert isinstance(entry[field], (int, float)) and entry[field] > 0, (key, month)
        assert entry['source_status'] == 'fixed', (key, month)
        assert entry['measurement'] and entry['notes'], (key, month)
        url = urlparse(entry['source'])
        assert url.scheme == 'https'
        if key.startswith('t_bill'):
            assert url.hostname == 'www.rbi.org.in' and url.query
            assert entry['data_date'].startswith(month), (key, month)
        elif key == 'ten_year_gsec_yield':
            assert url.hostname in ('www.rbi.org.in', 'www.fbil.org.in')
            assert url.query and 'semi-annual' in entry['measurement']
            if url.hostname == 'www.fbil.org.in':
                assert parse_qs(url.query)['date'] == [entry['data_date']]

groups = defaultdict(list)
dates = set()
for row in inputs['observations']:
    assert row['date'] not in dates, f'Duplicate NSE observation: {row["date"]}'
    dates.add(row['date'])
    groups[row['date'][:7]].append(Decimal(row['pe']))
assert groups.keys() == months
for month, values in groups.items():
    actual = (sum(values) / len(values)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    entry = data['nifty50_pe'][month]
    assert actual == Decimal(str(entry['pe_ratio'])), (month, actual, entry['pe_ratio'])
    assert entry['observation_count'] == len(values), month
    assert (ROOT / entry['calculation_source']).is_file()

# Selection exceptions must survive future maintenance.
for key in keys[:2]:
    assert data[key]['2026-03']['data_date'] == '2026-03-18'
    assert 'rejected' in data[key]['2026-03']['notes']
    assert data[key]['2026-09']['data_date'] == '2026-09-30'
print(f'Validated {len(months) * len(keys)} monthly entries and {len(dates)} daily NSE observations.')
