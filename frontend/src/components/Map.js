import React, { useEffect, useState } from 'react';
import { Chart } from 'react-google-charts';

export default function Map() {
    const [mapsData, setMapsData] = useState([]);

    useEffect(() => {
        return fetch('http://127.0.0.1:5000/maps/get_data')
            .then(response => response.json())
            .then(data => setMapsData(data))
            .catch(error => console.log(error))
    }, [])

    return (
        <Chart
            // width={'500px'}
            // height={'300px'}
            chartType="GeoChart"
            data={mapsData}
            mapsApiKey="AIzaSyAtpxG25mQR4mrbRH__lYtMvwJcRcB-lEs"
            rootProps={{ 'data-testid': '1' }}
            options={{
                colorAxis: { colors: ['#FFA8D3', '#C71C69'] },
                backgroundColor: '#B8E8F0',
                datalessRegionColor: '#FFA8D3',
            }}
        />
    )
}
