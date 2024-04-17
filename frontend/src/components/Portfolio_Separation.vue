<template>
   <div class="padtop">
     <apexchart type="donut" :options="chartOptions" :series="series" width="600" height="400"></apexchart>
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
       series: [25, 25, 10, 40],
       chartOptions: {
         labels: ['AAPL', 'GOOG', 'IBM', 'MSFT'],
         plotOptions: {
           pie: {
             donut: {
               size: '50%',
             },
             labels: {
                show: false,
              },
           },
         },
         colors: ['#5c97da'],
       },
     };
   },
 };
 </script>
 