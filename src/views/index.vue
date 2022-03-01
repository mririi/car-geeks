<template>
    <div class="layout-px-spacing dash_1">
        <portal to="breadcrumb">
            <ul class="navbar-nav flex-row">
                <li>
                    <div class="page-header">
                        <nav class="breadcrumb-one" aria-label="breadcrumb">
                            <ol class="breadcrumb">
                                <li class="breadcrumb-item active" aria-current="page"><span>Home</span></li>
                            </ol>
                        </nav>
                    </div>
                </li>
            </ul>

            
        </portal>

        
    </div>
</template>

<script>
    import Vue from 'vue';
    import VueApexCharts from 'vue-apexcharts';
    Vue.use(VueApexCharts);
    Vue.component('apexchart', VueApexCharts);

    import '@/assets/sass/widgets/widgets.scss';

    export default {
        metaInfo: { title: 'Sales Admin' },
        data() {
            return {
                //Daily Sales
                daily_sales_series: [
                    { name: 'Sales', data: [44, 55, 41, 67, 22, 43, 21] },
                    { name: 'Last Week', data: [13, 23, 20, 8, 13, 27, 33] }
                ],

                //Total Orders
                total_orders_series: [{ name: 'Sales', data: [28, 40, 36, 52, 38, 60, 38, 52, 36, 40] }],

                //Revenue
                revenue_series: [
                    { name: 'Income', data: [16800, 16800, 15500, 17800, 15500, 17000, 19000, 16000, 15000, 17000, 14000, 17000] },
                    { name: 'Expenses', data: [16500, 17500, 16200, 17300, 16000, 19500, 16000, 17000, 16000, 19000, 18000, 19000] }
                ],

                //Sales by Category
                sales_donut_series: [985, 737, 270]
            };
        },
        computed: {
            //Revenue
            revenue_options() {
                const is_dark = this.$store.state.is_dark_mode;
                return {
                    chart: {
                        fontFamily: 'Nunito, sans-serif',
                        zoom: { enabled: false },
                        toolbar: { show: false },
                        events: {
                            mounted: function(ctx) {
                                const highest1 = ctx.getHighestValueInSeries(0);
                                const highest2 = ctx.getHighestValueInSeries(1);

                                ctx.addPointAnnotation({
                                    x: 'Jul',
                                    y: highest1,
                                    label: { style: { cssClass: 'd-none' } },
                                    customSVG: {
                                        SVG:
                                            '<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="#1b55e2" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="feather feather-circle"><circle cx="12" cy="12" r="10"></circle></svg>',
                                        cssClass: undefined,
                                        offsetX: -8,
                                        offsetY: 7
                                    }
                                });

                                ctx.addPointAnnotation({
                                    x: 'Jun',
                                    y: highest2,
                                    label: { style: { cssClass: 'd-none' } },
                                    customSVG: {
                                        SVG:
                                            '<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="#e7515a" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="feather feather-circle"><circle cx="12" cy="12" r="10"></circle></svg>',
                                        cssClass: undefined,
                                        offsetX: -8,
                                        offsetY: 7
                                    }
                                });
                            }
                        }
                    },
                    dataLabels: { enabled: false },
                    stroke: { show: true, curve: 'smooth', width: 2, lineCap: 'square' },
                    dropShadow: { enabled: true, opacity: 0.2, blur: 10, left: -7, top: 22 },
                    colors: is_dark ? ['#2196f3', '#e7515a'] : ['#1b55e2', '#e7515a'],
                    markers: {
                        discrete: [
                            { seriesIndex: 0, dataPointIndex: 7, fillColor: '#000', strokeColor: '#000', size: 5 },
                            { seriesIndex: 2, dataPointIndex: 11, fillColor: '#000', strokeColor: '#000', size: 4 }
                        ]
                    },
                    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    xaxis: {
                        axisBorder: { show: false },
                        axisTicks: { show: false },
                        crosshairs: { show: true },
                        labels: { offsetX: 0, offsetY: 5, style: { fontSize: '12px', fontFamily: 'Nunito, sans-serif', cssClass: 'apexcharts-xaxis-title' } }
                    },
                    yaxis: {
                        tickAmount: 7,
                        labels: {
                            formatter: function(value) {
                                return value / 1000 + 'K';
                            },
                            offsetX: -10,
                            offsetY: 0,
                            style: { fontSize: '12px', fontFamily: 'Nunito, sans-serif', cssClass: 'apexcharts-yaxis-title' }
                        }
                    },
                    grid: {
                        borderColor: is_dark ? '#191e3a' : '#e0e6ed',
                        strokeDashArray: 5,
                        xaxis: { lines: { show: true } },
                        yaxis: { lines: { show: false } },
                        padding: { top: 0, right: 0, bottom: 0, left: 0 }
                    },
                    legend: {
                        position: 'top',
                        horizontalAlign: 'right',
                        offsetY: 0,
                        fontSize: '16px',
                        fontFamily: 'Nunito, sans-serif',
                        markers: { width: 10, height: 10, strokeWidth: 0, strokeColor: '#fff', fillColors: undefined, radius: 12, onClick: undefined, offsetX: 0, offsetY: 0 },
                        itemMargin: { horizontal: 20, vertical: 5 }
                    },
                    tooltip: { theme: 'dark', marker: { show: true }, x: { show: false } },
                    fill: {
                        type: 'gradient',
                        gradient: {
                            type: 'vertical',
                            shadeIntensity: 1,
                            inverseColors: !1,
                            opacityFrom: is_dark ? 0.19 : 0.28,
                            opacityTo: 0.05,
                            stops: is_dark ? [100, 100] : [45, 100]
                        }
                    }
                };
            },

            //Daily Sales
            daily_sales_options() {
                return {
                    chart: { toolbar: { show: false }, stacked: true, stackType: '100%' },
                    dataLabels: { enabled: false },
                    stroke: { show: true, width: 1 },
                    colors: ['#e2a03f', '#e0e6ed'],
                    responsive: [{ breakpoint: 480, options: { legend: { position: 'bottom', offsetX: -10, offsetY: 0 } } }],
                    xaxis: { labels: { show: false }, categories: ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat'] },
                    yaxis: { show: false },
                    fill: { opacity: 1 },
                    plotOptions: { bar: { horizontal: false, columnWidth: '25%' } },
                    legend: { show: false },
                    grid: {
                        show: false,
                        xaxis: { lines: { show: false } },
                        padding: { top: 10, right: -20, bottom: -20, left: -20 }
                    }
                };
            },

            //Total Orders
            total_orders_options() {
                const is_dark = this.$store.state.is_dark_mode;
                return {
                    chart: { sparkline: { enabled: true } },
                    stroke: { curve: 'smooth', width: 2 },
                    colors: is_dark ? ['#1abc9c'] : ['#fff'],
                    labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                    yaxis: { min: 0, show: false },
                    grid: { padding: { top: 125, right: 0, bottom: 0, left: 0 } },
                    fill: {
                        opacity: 1,
                        type: 'gradient',
                        gradient: {
                            type: 'vertical',
                            shadeIntensity: 1,
                            inverseColors: !1,
                            opacityFrom: is_dark ? 0.3 : 0.4,
                            opacityTo: 0.05,
                            stops: is_dark ? [100, 100] : [45, 100]
                        }
                    },
                    tooltip: { x: { show: false }, theme: 'dark' }
                };
            },

            //Sales by Category
            sales_donut_options() {
                const is_dark = this.$store.state.is_dark_mode;
                let option = {
                    chart: {},
                    dataLabels: { enabled: false },
                    expandOnClick: is_dark ? false : true,
                    stroke: { show: true, width: 25, colors: is_dark ? '#0e1726' : '#fff' },
                    colors: is_dark ? ['#5c1ac3', '#e2a03f', '#e7515a', '#e2a03f'] : ['#e2a03f', '#5c1ac3', '#e7515a'],
                    legend: {
                        position: 'bottom',
                        horizontalAlign: 'center',
                        fontSize: '14px',
                        markers: { width: 10, height: 10 },
                        height: 50,
                        offsetY: 20,
                        itemMargin: { horizontal: 8, vertical: 0 }
                    },
                    plotOptions: {
                        pie: {
                            donut: {
                                size: '65%',
                                background: 'transparent',
                                labels: {
                                    show: true,
                                    name: { show: true, fontSize: '29px', fontFamily: 'Nunito, sans-serif', offsetY: -10 },
                                    value: {
                                        show: true,
                                        fontSize: '26px',
                                        fontFamily: 'Nunito, sans-serif',
                                        color: is_dark ? '#bfc9d4' : undefined,
                                        offsetY: 16,
                                        formatter: function(val) {
                                            return val;
                                        }
                                    },
                                    total: {
                                        show: true,
                                        label: 'Total',
                                        color: '#888ea8',
                                        fontSize: '29px',
                                        formatter: function(w) {
                                            return w.globals.seriesTotals.reduce(function(a, b) {
                                                return a + b;
                                            }, 0);
                                        }
                                    }
                                }
                            }
                        }
                    },
                    labels: ['Apparel', 'Sports', 'Others']
                };

                if (is_dark) {
                    option['states'] = {
                        hover: { filter: { type: 'none' } },
                        active: { filter: { type: 'none' } }
                    };
                }

                return option;
            }
        },
        mounted() {},
        methods: {}
    };
</script>
