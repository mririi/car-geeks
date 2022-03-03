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

                               <router-link :to="'questionpage/'+q.id"> <b-card-title title-tag="h5">{{q.titleQ}}</b-card-title></router-link>
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
                                            <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    width="24"
                                    height="24"
                                    viewBox="0 0 24 24"
                                    fill="none"
                                    stroke="currentColor"
                                    stroke-width="2"
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="feather feather-thumbs-up"
                                >
                                    <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path>
                                </svg>
                                            {{q.nblikes}}
                                        </div>

                                        <div class="meta-view">
                                            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 14 14"><path fill="currentColor" d="M6.598 5.013a.144.144 0 0 1 .202.134V6.3a.5.5 0 0 0 .5.5c.667 0 2.013.005 3.3.822c.984.624 1.99 1.76 2.595 3.876c-1.02-.983-2.185-1.516-3.205-1.799a8.74 8.74 0 0 0-1.921-.306a7.404 7.404 0 0 0-.798.008h-.013l-.005.001h-.001L7.3 9.9l-.05-.498a.5.5 0 0 0-.45.498v1.153c0 .108-.11.176-.202.134L2.614 8.254a.503.503 0 0 0-.042-.028a.147.147 0 0 1 0-.252a.499.499 0 0 0 .042-.028l3.984-2.933zM7.8 10.386c.068 0 .143.003.223.006c.434.02 1.034.086 1.7.271c1.326.368 2.896 1.202 3.94 3.08a.5.5 0 0 0 .933-.305c-.464-3.71-1.886-5.662-3.46-6.66c-1.245-.79-2.527-.942-3.336-.971v-.66a1.144 1.144 0 0 0-1.767-.96l-3.994 2.94a1.147 1.147 0 0 0 0 1.946l3.994 2.94a1.144 1.144 0 0 0 1.767-.96v-.667z"/></svg>
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