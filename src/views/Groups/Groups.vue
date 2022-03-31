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
    
    <div class="col-xl-4 col-lg-6 col-md-6 col-sm-12 col-12 layout-spacing mt-5">
      <div class="widget widget-card-two">
          <span v-for="g in Groups" :key="g.id">
        <div class="widget-heading">
          <b-media>
            <template #aside>
              <div class="w-img">
                <img :src="'http://127.0.0.1:8000' + g.imageG" alt="avatar" />
              </div>
            </template>
            <h6>{{g.titleG}}</h6>
            <p class="meta-date-time">{{g.countryG}}</p>
          </b-media>
        </div>
        <div class="widget-content">
          <h5>{{g.nbmembers}} Members Going</h5>
          <div class="img-group">
            <img src="@/assets/images/profile-19.jpeg" alt="avatar" />
            <img src="@/assets/images/profile-6.jpeg" alt="avatar" />
            <img src="@/assets/images/profile-8.jpeg" alt="avatar" />
            <img src="@/assets/images/profile-3.jpeg" alt="avatar" />
          </div>
          <b-button :href="'/groupdetail/'+g.id" tag="a">View Details</b-button>
        </div>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  metaInfo: { title: 'Groups' },
  data() {
    return {};
  },
  created: function () {
    this.GetGroups();
  },
  mounted() {},
  computed: {
    ...mapGetters({
      Groups: 'StateGroups',
    }),
  },
  methods: {
    ...mapActions(['GetGroups']),
  },
};
</script>
