<template></template>
    <div>
        <h1>Dashboard</h1>
        <DisplayStocks />
    </div>
</template>

<script>
import DisplayStocks from "@/components/DisplayStocks.vue";

export default {
    name: "Dashboard",
    components: {
        DisplayStocks
    }
};
</script>

<style scoped>
/* Add your custom styles here */
</style>