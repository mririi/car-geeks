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
            <div id="flRegistrationForm" class="col-lg-12 layout-spacing">
              <div class="statbox panel box box-shadow">
                <div class="panel-heading">
                  <div class="row">
                    <div class="col-xl-10 col-md-12 col-sm-12 col-12">
                      <h4>Add Service</h4>
                    </div>
                  </div>
                </div>
                <div class="panel-body">
                  <b-form novalidate @submit.prevent="submit">
                    <label >Title <span style="color:red">*</span></label>
                    <b-form-group class="mb-3">
                      <b-input type="text" placeholder="Service title " v-model="form.titleS" :class="[is_submit_form1 ? (form.titleS && form.titleS.length<100 && form.titleS.length>15 ? 'is-valid' : 'is-invalid') : '']"></b-input>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.titleS  }">Please Enter a title between 15 and 100 characters</b-form-invalid-feedback>
                    </b-form-group>
                    <b-form-row class="mb-1">
                    <label class="col-6" >Address <span style="color:red">*</span></label>
                    <label >Price <span style="color:red">*</span></label>
                    </b-form-row>
                  <b-form-row>
                    <b-form-group class="col-6 mb-3">
                      <b-input  type="text" v-model="form.addressS" placeholder="Service Address" />
                    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.addressS }">Please Enter an address</b-form-invalid-feedback>
                    </b-form-group>
                    
                    <b-form-group class="col-6 mb-3">
                      <b-input type="text"  v-model="form.priceS" placeholder="Price" />
                    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.priceS }">Please Enter an address</b-form-invalid-feedback>
                    </b-form-group>
                    </b-form-row>
                    <b-form-row class="mb-1">
                    <b-form-group label="Phone Number" class="col-md-6">
                      <MazPhoneNumberInput Black v-model="form.contactS" :class="[is_submit_form1 ? (form.contactS ? 'is-valid' : 'is-invalid') : '']" />
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.contactS }">Please fill the Phone number</b-form-invalid-feedback>
                    </b-form-group>
                    <b-form-group class="col-md-6" label="Country">
                      <country-select
                        class="country-select"
                        v-model="form.country"
                        :country="form.country"
                        topCountry="US"
                        :class="[is_submit_form1 ? (form.country ? 'is-valid' : 'is-invalid') : '']"
                      />
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.country }">Please fill the Country</b-form-invalid-feedback>
                    </b-form-group>
                    </b-form-row>
                    <label >Insert image</label>
                    <div class="mb-4">
                      <b-file @change="onFileChanged"></b-file>
                    </div>
                    <label >Select Type <span style="color:red">*</span></label>
                    <b-select value="Default select" v-model="form.typeS" >
                      <b-select-option value="0">Select Type</b-select-option>
                      <b-select-option v-for="c in Servicetypes" :key="c.id" :value="c.id">{{c.descT}}</b-select-option>
                    </b-select>
                    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.typeS }">Please fill the Type</b-form-invalid-feedback>
                     <small id="emailHelp2" class="form-text text-muted mt-3"><span style="color:red">*</span> Required Fields</small>
                    <b-button  @click="submit" variant="primary" class="mt-4 justfiy-content-end">Submit</b-button>
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
        titleS: '',
        addressS: '',
        userprofileS:'',
        country:'',
        contactS:'',
        typeS:0
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
    this.GetServicetypes()
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
        this.$router.push('/auth/userinfo')
      }
  },
    methods: {
   onFileChanged (event) {
      this.image = event.target.files[0]
      console.log(this.image)
    },
    ...mapActions(["GetServicetypes","CreateService","GetUsers","GetUserprofiles"]),
    async submit() {
      try {
        this.is_submit_form1 = true;
                if (this.form.titleS && this.form.titleS.length<100 && this.form.titleS.length>15 &&
                  this.form.addressS &&
                  this.form.typeS &&
                  this.form.country &&
                  this.form.contactS
                ) {
        for (let u in this.Userprofiles){
      if(this.Userprofiles[u].userU==this.CurrentUser.id)
        {
          this.form.userprofileS=this.Userprofiles[u].id;
        }
      }
      var formdata = new FormData();
      if (this.image!=null)
      {
        formdata.append("imageS", this.image);
      }
        formdata.append("titleS", this.form.titleS);
        formdata.append("addressS", this.form.addressS);
        formdata.append("contactS", this.form.contactS);
        formdata.append("country", this.form.country);
        formdata.append("typeS", this.form.typeS);
        formdata.append("userprofiles", this.form.userprofileS);
        await this.CreateService(formdata);
        this.$router.push("/services");
        }
      } catch (error) {
        throw "Il ya un error!"
      }
    },
    
    },
    computed: {
    ...mapGetters({ Servicetypes:"StateServicetypes",Userprofiles:"StateUserprofiles", User: "StateUser",Users: "StateUsers"}),
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
    },
};
</script>