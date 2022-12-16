import untangle
import json
p = False
d = []
x = {}
with open('parseable.html', 'r') as f:
	for line in f.readlines():
		if '<img' in line: #
			x['img'] = line.split('/')[2].split('"')[0]
		if 'h5' in line: # name
			x['name'] = untangle.parse(line).h5.cdata
		if 'Age' in line:
			x['age'] = int(untangle.parse(line).p.cdata.strip())
			d.append(x)
			x = {}
print(json.dumps(d))
