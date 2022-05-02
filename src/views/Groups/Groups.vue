<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="javascript:;">Pages</a></li>
                <li class="breadcrumb-item active" aria-current="page"><span>Groups</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>
    <h3 class="mt-2"><b>Group List</b></h3>
    <div>
      <div class="mr-1 mt-3 d-flex justify-content-center w-25">
        <div class="col-lg-12 col-md-12 col-sm-12 filtered-list-search-live mx-auto">
          <b-form class="form-inline my-2 my-lg-0 justify-content-center" @submit.prevent="search">
            <div class="w-100">
              <b-input v-model="search" class="w-100 product-search br-25" placeholder="Search Groups" @keyup="search"></b-input>
            </div>
          </b-form>
        </div>
      </div>
    </div>
    <hr>
     
    <div class="row">
      <span v-for="g in filteredList" :key="g.id">
        <span v-if="g.accepted==true">
        <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 layout-spacing mt-1">
          <div class="widget widget-card-two">
            <div class="widget-heading">
              <b-media>
                <template #aside>
                  <div class="w-img">
                    <img :src=" g.imageG" alt="avatar" />
                  </div>
                </template>
                <h6>{{ g.titleG }}</h6>
                <p class="meta-date-time">{{ g.countryG }}</p>
              </b-media>
            </div>
            <div class="widget-content">
              <h5>{{ g.nbmembers }} Members</h5>
              <div class="img-group">
                <span v-for="m in Members" :key="m.id">
                  <span v-if="m.groupMem == g.id && m.accepted == true">
                      <span v-if="Userprofiles.find((u)=>u.id == m.userprofileMem)">
                        <img :src="Userprofiles.find((u)=>u.id == m.userprofileMem).imageU" alt="avatar" />
                      </span>
                      <span v-else-if="Userentreprises.find((u)=>u.id == m.userentrepriseMem)">
                        <img :src="Userentreprises.find((u)=>u.id == m.userentrepriseMem).imageE" alt="avatar" />
                      </span>
                  </span>
                </span>
              </div>
              <b-button :href="'/groupdetail/' + g.id" tag="a">View Details</b-button>
            </div>
          </div>
        </div>
      </span>
      </span>
    </div>
  </div>
</template>

<script>
import '@/assets/sass/widgets/widgets.scss';
import { mapGetters, mapActions } from 'vuex';
export default {
  metaInfo: { title: 'Groups' },
  data() {
    return {
      search:''
    };
  },
  created: function () {
    this.GetGroups();
    this.GetGroupmembers();
    this.GetUserprofiles();
    //let groupup=this.Groups.find((d)=>d.accepted==true && this.Members.find((m)=>m.groupMem==d.id)==null)
    //this.CreateGroupmember({ userprofileMem: this.CurrentUserProfile.id, groupMem: groupup.id , userentrepriseMem:this.CurrentUserEntreprise.id,accepted:true});  
  },
  mounted() {},
  computed: {
    ...mapGetters({
      Groups: 'StateGroups',
      Members: 'StateGroupmembers',
      Userprofiles: 'StateUserprofiles',
      Userentreprises: 'StateUserentreprises',
    }),
    filteredList() {
      return this.Groups.filter((grp) => {
        return grp.titleG.toLowerCase().includes(this.search.toLowerCase());
      });
    },
  },
  methods: {
    ...mapActions(['GetGroups', 'GetGroupmembers','GetUserentreprises', 'GetUserprofiles']),
  },
};
</script>
