import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

def func():
    filename = 'data/eq_data_1_day_m1.geojson'
    with open(filename) as f:
        try:
            all_eq_data = json.load(f)
        except:
            pass
    all_eq_dicts = all_eq_data['features']
    mags, lons, lats, texts = [], [], [], []
    for eq_dict in all_eq_dicts:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        title = eq_dict['properties']['title']
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        texts.append(title)
    print(len(all_eq_dicts))
    print(mags[:10])
    print(lons[:5])
    print(lats[:5])
    data =[{
        'type' : 'scattergeo',
        'lon'  : lons,
        'lat' : lats,
        'text': texts,
        'marker' : {
            'size' : [5*mag for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
        },
    }]
    my_layout = Layout(title='Earthquakes')
    fig = {'data' : data , 'layout' : my_layout }
    offline.plot(fig, filename='earthquakes.html')
    readable_file = 'data/readable_eq_data.json'
    with open(readable_file, 'w') as f :
        json.dump(all_eq_data, f, indent=4)
