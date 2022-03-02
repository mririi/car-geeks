import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from "axios";
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://127.0.0.1:8000/";
//bootstrap vue
import { BootstrapVue } from 'bootstrap-vue';
import 'bootstrap-vue/dist/bootstrap-vue.css';
Vue.use(BootstrapVue);

//phone number
import MazPhoneNumberInput from 'maz-ui'
Vue.use(MazPhoneNumberInput)
import VuePhoneNumberInput from 'vue-phone-number-input';
import 'vue-phone-number-input/dist/vue-phone-number-input.css';
Vue.component('vue-phone-number-input', VuePhoneNumberInput);
//perfect scrollbar
import PerfectScrollbar from 'vue2-perfect-scrollbar';
Vue.use(PerfectScrollbar);

import vueCountryRegionSelect from 'vue-country-region-select'
Vue.use(vueCountryRegionSelect)


//vue-scrollactive
import VueScrollactive from 'vue-scrollactive';
Vue.use(VueScrollactive);

//vue-meta
import VueMeta from 'vue-meta';
Vue.use(VueMeta, {
    refreshOnceOnNavigation: true
});

//Sweetalert
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
const options = {
    confirmButtonColor: '#4361ee',
    cancelButtonColor: '#e7515a'
};
Vue.use(VueSweetalert2, options);

//portal vue
import PortalVue from 'portal-vue';
Vue.use(PortalVue);

//vue-i18n
import i18n from './i18n';

Vue.config.productionTip = false;

// set default settings
import appSetting from './app-setting';
Vue.prototype.$appSetting = appSetting;
appSetting.init();

new Vue({
    router,
    store,
    i18n,
    render: h => h(App)
}).$mount('#app');
