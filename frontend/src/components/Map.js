import React from 'react';
import { Chart } from 'react-google-charts';

export default function Map () {
    return (
        <Chart
            // width={'500px'}
            // height={'300px'}
            chartType="GeoChart"
            data={[
                ['Country', 'Popularity'],
                ['Germany', 200],
                ['United States', 300],
                ['Brazil', 400],
                ['Canada', 500],
                ['France', 600],
                ['RU', 700],
            ]}
            mapsApiKey="AIzaSyAtpxG25mQR4mrbRH__lYtMvwJcRcB-lEs"
            rootProps={{ 'data-testid': '1' }}
        />
    )
}