<template>
  <div id="chartDonut" class="col-xl-12 layout-spacing">
                   
                </div>
</template>

<script>
import Vue from 'vue';
    import VueApexCharts from 'vue-apexcharts';
    Vue.use(VueApexCharts);
    Vue.component('apexchart', VueApexCharts);
export default {
     data() {
            return {
                 series_7: [44, 55, 41, 17],
            };
     },
 computed:{
options_7() {
                const is_dark = this.$store.state.is_dark_mode;
                return {
                    chart: { toolbar: { show: false } },
                    stroke: { colors: is_dark ? '#191e3a' : 'transparent' },
                    responsive: [{ breakpoint: 480, options: { chart: { width: 200 }, legend: { position: 'bottom' } } }]
                };
            },
 },
}
</script>

<style>

</style>