<template>
  <div :class="[$store.state.layout_style, $store.state.menu_style]">
    <component v-bind:is="layout"></component>
  </div>
</template>
<script>
// layouts
import appLayout from './layouts/app-layout.vue';
import authLayout from './layouts/auth-layout.vue';
import axios from 'axios';
import '@/assets/sass/app.scss';
import questionLayout from './layouts/question-layout.vue';
import serviceLayout from './layouts/service-layout.vue';
import dashboardLayout from './layouts/dashboard-layout.vue';
import { mapGetters, mapActions } from 'vuex';
import groupLayout from './layouts/group-layout.vue';
export default {
  metaInfo: {
    title: 'Home',
    titleTemplate: '%s | Car Geeks',
  },
  components: {
    app: appLayout,
    auth: authLayout,
    question: questionLayout,
    service: serviceLayout,
    dashboard: dashboardLayout,
    group: groupLayout,
  },
  computed: {
    layout() {
      return this.$store.getters.layout;
    },
    ...mapGetters({
      Userprofiles: 'StateUserprofiles',
    }),
  },
  data() {
    return {};
  },
  created() {
    this.GetUserprofiles();
    for (let u in this.Userprofiles) {
      if (this.Userprofiles[u].nbquestions >= 10 && this.Userprofiles[u].nbquestions < 20) {
        axios.put('/userprofile/userprofile-update/' + this.Userprofiles[u].id + '/', { badgeU: 1 });
      } else if (this.Userprofiles[u].nbquestions >= 20 && this.Userprofiles[u].nbquestions < 30) {
        axios.put('/userprofile/userprofile-update/' + this.Userprofiles[u].id + '/', { badgeU: 2 });
      } else if (this.Userprofiles[u].nbquestions >= 30) {
        axios.put('/userprofile/userprofile-update/' + this.Userprofiles[u].id + '/', { badgeU: 3 });
      }
    }
  },
  mounted() {},
  methods: {
    ...mapActions(['GetUserprofiles']),
  },
};
</script>
