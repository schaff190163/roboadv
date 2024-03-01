<template>
  <div>
    <apexchart type="line" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  setup() {
    const chartOptions = ref({
      chart: {
        id: 'vuechart-example'
      },
      xaxis: {
        type: 'datetime'
      }
    })

    const series = ref([{
      name: 'stock',
      data: []
    }])

    async function getStockData() {
      const response = await fetch('http://localhost:8000/api/stockdata')
      const data = await response.json()
      series.value[0].data = Object.entries(data['Time Series (Daily)']).map(([date, value]) => {
        return {
          x: new Date(date),
          y: parseFloat(value['4. close'])
        }
      })
    }

    onMounted(getStockData)

    return {
      chartOptions,
      series
    }
  }
}
</script>