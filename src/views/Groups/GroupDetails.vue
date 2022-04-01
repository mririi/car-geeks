<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="javascript:;">Groups</a></li>
                <li class="breadcrumb-item active" aria-current="page"><span>Group Details</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>
    <div id="card_8" class="col-lg-12 layout-spacing mt-3">
      <div class="panel-heading">
        <div class="row"></div>
      </div>
      <div class="panel-body">
        <b-card :img-src="'http://127.0.0.1:8000' + group.imageG" img-width="100%" img-height="290px" img-top class="component-card_8">
          <div class="progress-order">
            <div class="progress-order-header">
              <div class="row">
                <div class="col-md-6 col-sm-6 col-12">
                  <h2>
                    <b>{{ group.titleG }}</b>
                  </h2>
                  <h6>Private Group</h6>
                </div>
                <div class="col-md-6 pl-0 col-sm-6 col-12 text-right">
                  <span v-if="group.userprofileG != CurrentUserProfile.id">
                  <b-button variant="primary"  @click="Join()"
                    ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                      <path
                        fill="currentColor"
                        d="M22 9V7h-2v2h-2v2h2v2h2v-2h2V9zM8 12c2.21 0 4-1.79 4-4s-1.79-4-4-4s-4 1.79-4 4s1.79 4 4 4zm0 1c-2.67 0-8 1.34-8 4v3h16v-3c0-2.66-5.33-4-8-4zm4.51-8.95C13.43 5.11 14 6.49 14 8s-.57 2.89-1.49 3.95C14.47 11.7 16 10.04 16 8s-1.53-3.7-3.49-3.95zm4.02 9.78C17.42 14.66 18 15.7 18 17v3h2v-3c0-1.45-1.59-2.51-3.47-3.17z"
                      />
                    </svg>
                    Join Group</b-button
                  >
                  </span>
                  <span v-else>
                   <b-button variant="primary"  :href="'/groupdashboard/'+group.id+'/dashboard'"
                    ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 36 36"><path fill="currentColor" d="M12 16.14h-.87a8.67 8.67 0 0 0-6.43 2.52l-.24.28v8.28h4.08v-4.7l.55-.62l.25-.29a11 11 0 0 1 4.71-2.86A6.58 6.58 0 0 1 12 16.14Z" class="clr-i-solid--badged clr-i-solid-path-1--badged"/><path fill="currentColor" d="M31.34 18.63a8.67 8.67 0 0 0-6.43-2.52a10.47 10.47 0 0 0-1.09.06a6.59 6.59 0 0 1-2 2.45a10.91 10.91 0 0 1 5 3l.25.28l.54.62v4.71h3.94v-8.32Z" class="clr-i-solid--badged clr-i-solid-path-2--badged"/><path fill="currentColor" d="M11.1 14.19h.31a6.45 6.45 0 0 1 3.11-6.29a4.09 4.09 0 1 0-3.42 6.33Z" class="clr-i-solid--badged clr-i-solid-path-3--badged"/><circle cx="17.87" cy="13.45" r="4.47" fill="currentColor" class="clr-i-solid--badged clr-i-solid-path-4--badged"/><path fill="currentColor" d="M18.11 20.3A9.69 9.69 0 0 0 11 23l-.25.28v6.33a1.57 1.57 0 0 0 1.6 1.54h11.49a1.57 1.57 0 0 0 1.6-1.54V23.3l-.24-.3a9.58 9.58 0 0 0-7.09-2.7Z" class="clr-i-solid--badged clr-i-solid-path-5--badged"/><path fill="currentColor" d="M24.43 13.44a6.54 6.54 0 0 1 0 .69a4.09 4.09 0 0 0 .58.05h.19a4.05 4.05 0 0 0 2.52-1a7.5 7.5 0 0 1-5.14-6.32A4.13 4.13 0 0 0 21.47 8a6.53 6.53 0 0 1 2.96 5.44Z" class="clr-i-solid--badged clr-i-solid-path-6--badged"/><circle cx="30" cy="6" r="5" fill="currentColor" class="clr-i-solid--badged clr-i-solid-path-7--badged clr-i-badge"/><path fill="none" d="M0 0h36v36H0z"/></svg>
                    Manage Group</b-button
                  >
                  </span>
                </div>
              </div>
            </div>

            <div class="progress-order-body">
              <div class="row mt-4">
                <div class="col-md-12">
                  <ul class="list-inline badge-collapsed-img mb-0 mb-3">
                    
                    <span v-for="m in Members" :key="m.id">
                      <span v-if="m.groupMem==group.id && m.userprofileMem && m.accepted==true">
                        <span v-for="uu in Userprofiles.slice(0, 4)" :key="uu.id">
                          <span v-if="uu.id == m.userprofileMem">
                        <li class="list-inline-item chat-online-usr">
                          <router-link :to="'/profile/'+uu.id">
                          <img alt="avatar" :src="'http://127.0.0.1:8000' + uu.imageU" class="ml-0" />
                          </router-link>
                        </li>
                      </span>
                    </span>
                      </span>
                    </span>
                    <li class="list-inline-item badge-notify">
                      <div class="notification">
                        <span class="badge badge-info badge-pill">+{{ group.nbmembers - 4 }} more</span>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </b-card>
      </div>
    </div>
    <div class="row layout-top-spacing">
      <div id="timelineProfile" class="col-xl-12 layout-spacing">
        <div class="panel-heading">
          <div class="row"></div>
        </div>
        <div class="panel-body">
          <div class="timeline-simple">
            <p class="timeline-title">Group Posts</p>

            <div class="timeline-list">
              <span v-for="p in GroupPost" :key="p.id">
                <span v-if="p.groupPost == group.id && p.accepted == true">
                  <span v-for="u in Userprofiles" :key="u.id">
                    <span v-if="u.id == p.userprofilePost">
                      <div class="timeline-post-content">
                        <div class="user-profile">
                          <img :src="'http://127.0.0.1:8000' + u.imageU" img-top alt="" />
                        </div>

                        <div class="">
                          <h4>{{ u.firstname }} {{ u.lastname }}</h4>
                          <p class="meta-time-date">{{ p.datecreation | formatDate }}</p>

                          <div class="">
                            <h6 class="post-text">
                              {{ p.detailsP }}
                            </h6>
                          </div>
                          <div class="post-gallery-img col-md-12" v-if="p.imagePost != null">
                            <img :src="'http://127.0.0.1:8000' + p.imagePost" style="width: 400px; height: 200px" />
                          </div>
                          <div class="media-notation mb-5">
                            <a href="javascript:void(0);" class="mr-5"
                              ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16">
                                <path
                                  fill="currentColor"
                                  d="M8.864.046C7.908-.193 7.02.53 6.956 1.466c-.072 1.051-.23 2.016-.428 2.59c-.125.36-.479 1.013-1.04 1.639c-.557.623-1.282 1.178-2.131 1.41C2.685 7.288 2 7.87 2 8.72v4.001c0 .845.682 1.464 1.448 1.545c1.07.114 1.564.415 2.068.723l.048.03c.272.165.578.348.97.484c.397.136.861.217 1.466.217h3.5c.937 0 1.599-.477 1.934-1.064a1.86 1.86 0 0 0 .254-.912c0-.152-.023-.312-.077-.464c.201-.263.38-.578.488-.901c.11-.33.172-.762.004-1.149c.069-.13.12-.269.159-.403c.077-.27.113-.568.113-.857c0-.288-.036-.585-.113-.856a2.144 2.144 0 0 0-.138-.362a1.9 1.9 0 0 0 .234-1.734c-.206-.592-.682-1.1-1.2-1.272c-.847-.282-1.803-.276-2.516-.211a9.84 9.84 0 0 0-.443.05a9.365 9.365 0 0 0-.062-4.509A1.38 1.38 0 0 0 9.125.111L8.864.046zM11.5 14.721H8c-.51 0-.863-.069-1.14-.164c-.281-.097-.506-.228-.776-.393l-.04-.024c-.555-.339-1.198-.731-2.49-.868c-.333-.036-.554-.29-.554-.55V8.72c0-.254.226-.543.62-.65c1.095-.3 1.977-.996 2.614-1.708c.635-.71 1.064-1.475 1.238-1.978c.243-.7.407-1.768.482-2.85c.025-.362.36-.594.667-.518l.262.066c.16.04.258.143.288.255a8.34 8.34 0 0 1-.145 4.725a.5.5 0 0 0 .595.644l.003-.001l.014-.003l.058-.014a8.908 8.908 0 0 1 1.036-.157c.663-.06 1.457-.054 2.11.164c.175.058.45.3.57.65c.107.308.087.67-.266 1.022l-.353.353l.353.354c.043.043.105.141.154.315c.048.167.075.37.075.581c0 .212-.027.414-.075.582c-.05.174-.111.272-.154.315l-.353.353l.353.354c.047.047.109.177.005.488a2.224 2.224 0 0 1-.505.805l-.353.353l.353.354c.006.005.041.05.041.17a.866.866 0 0 1-.121.416c-.165.288-.503.56-1.066.56z"
                                />
                              </svg>
                              {{ p.nblikes }} Likes
                            </a>
                            <a href="javascript:void(0);" v-b-toggle="collapseComment(p.id)" class=""
                              ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1.28em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1792 1408">
                                <path
                                  fill="currentColor"
                                  d="M1408 512q0 139-94 257t-256.5 186.5T704 1024q-86 0-176-16q-124 88-278 128q-36 9-86 16h-3q-11 0-20.5-8t-11.5-21q-1-3-1-6.5t.5-6.5t2-6l2.5-5l3.5-5.5l4-5l4.5-5l4-4.5q5-6 23-25t26-29.5t22.5-29t25-38.5t20.5-44Q142 841 71 736T0 512q0-139 94-257T350.5 68.5T704 0t353.5 68.5T1314 255t94 257zm384 256q0 120-71 224.5T1526 1169q10 24 20.5 44t25 38.5t22.5 29t26 29.5t23 25q1 1 4 4.5t4.5 5t4 5t3.5 5.5l2.5 5l2 6l.5 6.5l-1 6.5q-3 14-13 22t-22 7q-50-7-86-16q-154-40-278-128q-90 16-176 16q-271 0-472-132q58 4 88 4q161 0 309-45t264-129q125-92 192-212t67-254q0-77-23-152q129 71 204 178t75 230z"
                                />
                              </svg>
                              {{ p.nbcomments }} Comments
                            </a>
                          </div>
                          <b-collapse :id="'collapse-hd-statistics-' + p.id" accordion="helpdesk-accordion" class="mb-5 col-xl-12">
                            <span v-for="c in Comments" :key="c.id">
                              <span v-if="c.postCom == p.id">
                                <b-card-body>
                                  <span v-for="up in Userprofiles" :key="up.id">
                                    <span v-if="c.userprofileCom == up.id">
                                      <b-media>
                                        <template #aside>
                                          <router-link :to="'/profile/' + up.id" class="text-primary">
                                            <b-avatar :src="'http://127.0.0.1:8000' + up.imageU" class="avatar-title rounded-circle mr-5"></b-avatar>
                                          </router-link>
                                          <p class="mt-2">{{ c.contentCom }}</p>
                                        </template>
                                      </b-media>
                                    </span>
                                  </span>
                                </b-card-body>
                              </span>
                            </span>
                          </b-collapse>
                        </div>
                      </div>
                    </span>
                  </span>
                </span>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import '@/assets/sass/scrollspyNav.scss';
import '@/assets/sass/components/timeline/custom-timeline.scss';
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';
export default {
  metaInfo: { title: 'Groups' },
  data() {
    return {
      group: [],
      CurrentUser: [],
      CurrentUserProfile: [],
    };
  },
  created: function () {
    this.GetGroups();
    this.GetGroupposts();
    this.GetUserprofiles();
    this.GetGroupcomments();
    this.GetGroupmembers();
    this.GetUsers();
    axios.get('/group/group-detail/' + this.$route.params.id + '/').then((response) => {
      this.group = response.data;
   
   for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let u in this.Userprofiles) {
      if (this.Userprofiles[u].userU == this.CurrentUser.id) {
        this.CurrentUserProfile = this.Userprofiles[u];
      }
    }
    });
  },
  mounted() {},
  computed: {
    ...mapGetters({
      Groups: 'StateGroups',
      GroupPost: 'StateGroupposts',
      Userprofiles: 'StateUserprofiles',
      Comments: 'StateGroupcomments',
      Members: 'StateGroupmembers',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
  },
  methods: {
    ...mapActions(['GetGroups', 'GetGroupposts','GetUsers', 'GetUserprofiles', 'GetGroupcomments', 'GetGroupmembers','CreateGroupmember']),

    collapseComment(i) {
      return 'collapse-hd-statistics-' + i;
    },

    Join()
    {
       this.CreateGroupmember({userprofileMem:this.CurrentUserProfile.id , groupMem:this.group.id});
    }
  },
};
</script>
<style scoped>
</style>