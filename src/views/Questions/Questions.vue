<template>
    <div class="layout-px-spacing">
        <portal to="breadcrumb">
            <ul class="navbar-nav flex-row">
                <li>
                    <div class="page-header">
                        <nav class="breadcrumb-one" aria-label="breadcrumb">
                            <ol class="breadcrumb">
                                <li class="breadcrumb-item active" aria-current="page"><span>Questions</span></li>
                            </ol>
                        </nav>
                    </div>
                </li>
            </ul>
        </portal>

        <div class="row layout-top-spacing">
            <div class="col-xl-12 col-md-12 col-sm-12 col-12">
                        <div class="panel-body">
                            <b-card class="component-card_9" v-for="q in Questions" :key="q.id">
                                <p class="meta-date">{{q.dateQ | formatDate}}</p>

                                <b-card-title title-tag="h5">{{q.titleQ}}</b-card-title>
                                <b-card-text>{{q.contentQ}}</b-card-text>

                                <div class="meta-info">
                                    <div class="meta-user">
                                        <div class="avatar avatar-sm">
                                            <span class="avatar-title rounded-circle">AG</span>
                                        </div>
                                        <div class="user-name">{{q.userprofileQ}}</div>
                                    </div>

                                    <div class="meta-action">
                                        <div class="meta-likes">
                                            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.93em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1536 1664"><path fill="currentColor" d="M256 1344q0-26-19-45t-45-19t-45 19t-19 45t19 45t45 19t45-19t19-45zm1152-576q0-51-39-89.5t-89-38.5H928q0-58 48-159.5t48-160.5q0-98-32-145t-128-47q-26 26-38 85t-30.5 125.5T736 448q-22 23-77 91q-4 5-23 30t-31.5 41t-34.5 42.5t-40 44t-38.5 35.5t-40 27t-35.5 9h-32v640h32q13 0 31.5 3t33 6.5t38 11t35 11.5t35.5 12.5t29 10.5q211 73 342 73h121q192 0 192-167q0-26-5-56q30-16 47.5-52.5t17.5-73.5t-18-69q53-50 53-119q0-25-10-55.5t-25-47.5q32-1 53.5-47t21.5-81zm128-1q0 89-49 163q9 33 9 69q0 77-38 144q3 21 3 43q0 101-60 178q1 139-85 219.5t-227 80.5H960q-96 0-189.5-22.5T554 1576q-116-40-138-40H128q-53 0-90.5-37.5T0 1408V768q0-53 37.5-90.5T128 640h274q36-24 137-155q58-75 107-128q24-25 35.5-85.5T712 145t62-108q39-37 90-37q84 0 151 32.5T1117 134t35 186q0 93-48 192h176q104 0 180 76t76 179z"/></svg>
                                            {{q.nblikes}}
                                        </div>

                                        <div class="meta-view">
                                            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><path fill="currentColor" d="M6.598 5.013a.144.144 0 0 1 .202.134V6.3a.5.5 0 0 0 .5.5c.667 0 2.013.005 3.3.822c.984.624 1.99 1.76 2.595 3.876c-1.02-.983-2.185-1.516-3.205-1.799a8.74 8.74 0 0 0-1.921-.306a7.404 7.404 0 0 0-.798.008h-.013l-.005.001h-.001L7.3 9.9l-.05-.498a.5.5 0 0 0-.45.498v1.153c0 .108-.11.176-.202.134L2.614 8.254a.503.503 0 0 0-.042-.028a.147.147 0 0 1 0-.252a.499.499 0 0 0 .042-.028l3.984-2.933zM7.8 10.386c.068 0 .143.003.223.006c.434.02 1.034.086 1.7.271c1.326.368 2.896 1.202 3.94 3.08a.5.5 0 0 0 .933-.305c-.464-3.71-1.886-5.662-3.46-6.66c-1.245-.79-2.527-.942-3.336-.971v-.66a1.144 1.144 0 0 0-1.767-.96l-3.994 2.94a1.147 1.147 0 0 0 0 1.946l3.994 2.94a1.144 1.144 0 0 0 1.767-.96v-.667z"/></svg>
                                            {{q.nbrep}}
                                        </div>
                                    </div>
                                </div>
                            </b-card>

                            </div>
                        </div>
                    </div>
                </div>
</template>
<style scoped>
    .layout-px-spacing {
        min-height: calc(100vh - 170px) !important;
    }
</style>
<script>
import moment from "moment";
import Vue from "vue";
Vue.filter("formatDate", function (value) {
  if (value) {
    return moment(String(value)).format("DD MMMM YYYY H:mm");
  }
});
import '@/assets/sass/components/cards/card.scss';
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Questions",
  components: {
    
  },
  data() {
    return {
      
     
    };
  },
  created: function () {
    this.GetQuestions();
   
  },
  computed: {
    ...mapGetters({
      Questions: "StateQuestions",
      
    }),
  },
  methods: {
    ...mapActions([
      "GetQuestions",
    ]),
  },
};
</script>