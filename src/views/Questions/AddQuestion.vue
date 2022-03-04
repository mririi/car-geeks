<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Add Question</span></li>
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
            <div id="flRegistrationForm" class="col-lg-10 layout-spacing">
              <div class="statbox panel box box-shadow">
                <div class="panel-heading">
                  <div class="row">
                    <div class="col-xl-10 col-md-12 col-sm-12 col-12">
                      <h4>Add Question</h4>
                    </div>
                  </div>
                </div>
                <div class="panel-body">
                  <b-form>
                    <b-form-group class="mb-4">
                      <b-input type="text" placeholder="Question title " v-model="form.titleQ" :class="[is_submit_form1 ? (form.titleQ ? 'is-valid' : 'is-invalid') : '']"></b-input>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.titleQ }">Please fill the Address</b-form-invalid-feedback>
                    </b-form-group>
                    <b-form-group class="mb-4">
                      <b-textarea rows="4" type="text" v-model="form.contentQ" placeholder="Question details"></b-textarea>
                    </b-form-group>
                    <div class="mb-5">
                      <b-file @change="onFileChanged"></b-file>
                    </div>

                    <b-select value="Default select">
                      <b-select-option value="Default select">Select Category</b-select-option>
                      <b-select-option v-for="c in Questioncategories" :key="c.id" :value="c.id">{{c.typeC}}</b-select-option>
                       
                    </b-select>
                   
                    <b-button  @click="submit" variant="primary" class="mt-4">Submit</b-button>
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
        userprofileQ:'',
        categoryQ:''
      },
      image:null,
      uprofile:[],
      CurrentUser:[],
      is_submit_form1:false, 
    };
  },
  created: function() {
    this.GetUsers()
    this.GetUserprofiles()
    this.GetQuestioncategories()
    for (let u in this.Users){
      if(this.Users[u].username==this.User)
        {
          this.CurrentUser = this.Users[u];
        }
      }
      let existuserprofile=false
      for (let uu in this.Userprofiles){
      if(this.Userprofiles[uu].userU==this.CurrentUser.id)
        {
          existuserprofile = true
        }
      }
      if (existuserprofile==false){
        this.$router.push('/userinfo')
      }
  },
    methods: {
   onFileChanged (event) {
      this.image = event.target.files[0]
      console.log(this.image)
    },
    ...mapActions(["GetQuestioncategories","CreateQuestion","GetUsers","GetUserprofiles"]),
    async submit() {
      try {
        for (let u in this.Userprofiles){
      if(this.Userprofiles[u].userU==this.CurrentUser.id)
        {
          this.form.userprofileQ=this.Userprofiles[u].id;
          this.uprofile = this.Userprofiles[u];
        }
      }
      var formdata = new FormData();
      if (this.image!=null)
      {
        formdata.append("imageQ", this.image);
      }
        formdata.append("titleQ", this.form.titleQ);
        formdata.append("contentQ", this.form.contentQ);
        formdata.append("categoryQ", this.form.categoryQ);
        formdata.append("userprofileQ", this.form.userprofileQ);
        console.log(this.form.categoryQ)
        await this.CreateQuestion(formdata);
        await axios.put('/userprofile/userprofile-update/' + this.form.userprofileQ +'/',{nbquestions:this.uprofile.nbquestions+=1})
        this.$router.push("/questions");
      } catch (error) {
        throw "Il ya un error!"
      }
    },
    },
    computed: {
    ...mapGetters({ Questioncategories:"StateQuestioncategories",Userprofiles:"StateUserprofiles", User: "StateUser",Users: "StateUsers"}),
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
    },
};
</script>