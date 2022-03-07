<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Update Question</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="row layout-top-spacing">
      <div class="col-xl-12 col-md-12 col-sm-12 col-12">
        <div class="panel-body">
          <div class="row">
            <div id="flRegistrationForm" class="col-lg-12 layout-spacing">
              <div class="statbox panel box box-shadow">
                <div class="panel-heading">
                  <div class="row">
                    <div class="col-xl-12 col-md-12 col-sm-12 col-12">
                      <h4>Update your Question</h4>
                    </div>
                  </div>
                </div>
                <div class="panel-body">
                  <b-form>
                    <label>Question title</label>
                    <b-form-group class="mb-3">
                      <b-input type="text" placeholder="Question title " v-model="form.titleQ" :class="[is_submit_form1 ? (form.titleQ ? 'is-valid' : 'is-invalid') : '']"></b-input>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.titleQ }">Please fill the Address</b-form-invalid-feedback>
                    </b-form-group>
                    <label>Question details</label>
                    <b-form-group class="mb-3">
                      <b-textarea rows="4" type="text" v-model="form.contentQ" placeholder="Question details"></b-textarea>
                    </b-form-group>
                    <label>Question image</label>
                    <div class="mb-4">
                      <b-file @change="onFileChanged"></b-file>
                    </div>
                    <label>Question Category</label>
                    <b-select value="Default select" v-model="form.categoryQ">
                      <b-select-option value="Default select">Select Category</b-select-option>
                      <b-select-option v-for="c in Questioncategories" :key="c.id" :value="c.id">{{ c.typeC }}</b-select-option>
                    </b-select>
                    <b-button @click="submit" variant="primary" class="mt-4 col-lg-3 ">Submit</b-button>
                  </b-form>
                </div>
              </div>
            </div>
          </div>
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
import moment from 'moment';
import Vue from 'vue';
import axios from 'axios';
Vue.filter('formatDate', function (value) {
  if (value) {
    return moment(String(value)).format('DD MMMM YYYY H:mm');
  }
});
import '@/assets/sass/components/cards/card.scss';
import '@/assets/sass/forms/file-upload-with-preview.min.css';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'Questions',
  components: {},
  data() {
    return {
      form: {
        titleQ: '',
        contentQ: '',
        userprofileQ: '',
        categoryQ: '',
      },
      image: null,
      uprofile: [],
      CurrentUser: [],
      is_submit_form1: false,
    };
  },
  created: function () {
    this.GetUsers();
    this.GetUserprofiles();
    this.GetQuestioncategories();
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    let existuserprofile = false;
    for (let uu in this.Userprofiles) {
      if (this.Userprofiles[uu].userU == this.CurrentUser.id) {
        existuserprofile = true;
      }
    }
    if (existuserprofile == false) {
      this.$router.push('/auth/userinfo');
    }
    axios.get('/question/question-detail/' + this.$route.params.id + '/').then((response) => {
      this.form = response.data;
    });
  },
  methods: {
    onFileChanged(event) {
      this.image = event.target.files[0];
      console.log(this.image);
    },
    ...mapActions(['GetQuestioncategories', 'CreateQuestion', 'GetUsers', 'GetUserprofiles']),
    async submit() {
      try {
        var formdata = new FormData();
        if (this.image != null) {
          formdata.append('imageQ', this.image);
        }
        formdata.append('titleQ', this.form.titleQ);
        formdata.append('contentQ', this.form.contentQ);
        formdata.append('categoryQ', this.form.categoryQ);
        formdata.append('accepted', false);
        axios.put('/question/question-update/' + this.$route.params.id + '/', formdata);
        this.$router.push('/questions');
        this.$router.go();
      } catch (error) {
        throw 'Il ya un error!';
      }
    },
  },
  computed: {
    ...mapGetters({ Questioncategories: 'StateQuestioncategories', Userprofiles: 'StateUserprofiles', User: 'StateUser', Users: 'StateUsers' }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
  },
};
</script>