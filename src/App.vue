<template>
    <div :class="[$store.state.layout_style, $store.state.menu_style]">
        <component v-bind:is="layout"></component>
    </div>
</template>
<script>
    // layouts
    import appLayout from './layouts/app-layout.vue';
    import authLayout from './layouts/auth-layout.vue';
    
    import '@/assets/sass/app.scss';
import questionLayout from './layouts/question-layout.vue';
import serviceLayout from './layouts/service-layout.vue';
import dashboardLayout from './layouts/dashboard-layout.vue';

    export default {
        metaInfo: {
            title: 'Home',
            titleTemplate: '%s | Car Geeks'
        },
        components: {
            app: appLayout,
            auth: authLayout,
            question: questionLayout,
            service: serviceLayout,
            dashboard: dashboardLayout
        },
        computed: {
            layout() {
                return this.$store.getters.layout;
            }
        },
        data() {
            return {};
        },
        mounted() {},
        methods: {}
    };
</script>
