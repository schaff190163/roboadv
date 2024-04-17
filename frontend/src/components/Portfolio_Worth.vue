<template>
  <div class="padtop">
    <apexchart type="line" :options="chartOptions" :series="chartSeries" width="800" height="400"></apexchart>
    <router-link to="/">DashBoard</router-link>
  </div>
</template>

<script>
import VueApexCharts from 'vue3-apexcharts';

export default {
  components: {
    apexchart: VueApexCharts,
  },
  data() {
    return {
      chartOptions: {
        chart: {
          id: 'portfolio-chart',
          toolbar: {
            show: false,
          },
        },
        xaxis: {
          categories: [],
        },
        colors: ['#5c97da', '#c1deff', '#c1deff', '#c1deff', '#c1deff'],
        legend: {
          show: true,
        },
      },
      chartSeries: [
        { name: 'Total', data: [] },
        { name: 'AAPL', data: [] },
        { name: 'GOOG', data: [] },
        { name: 'IBM', data: [] },
        { name: 'MSFT', data: [] },
      ],
    };
  },
  mounted() {
    const historicalData = [
      { date: '2022-01-01', AAPL: 100, GOOG: 200, IBM: 150, MSFT: 120 },
      { date: '2022-01-02', AAPL: 110, GOOG: 210, IBM: 160, MSFT: 130 },
      { date: '2022-01-03', AAPL: 110, GOOG: 180, IBM: 130, MSFT: 120 },
    ];
    this.chartOptions.xaxis.categories = historicalData.map((entry) => entry.date);
    this.chartSeries[0].data = historicalData.map((entry) => {
      return Object.values(entry).slice(1).reduce((total, value) => total + value, 0);
    });
    this.chartSeries.slice(1).forEach((series, index) => {
      series.data = historicalData.map((entry) => entry[Object.keys(entry)[index + 1]]);
    });
  },
};
</script>
