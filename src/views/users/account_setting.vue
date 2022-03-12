<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Profile Edit</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="account-settings-container layout-top-spacing">
      <div class="account-content">
        <div class="scrollspy-example" data-spy="scroll" data-target="#account-settings-scroll" data-offset="-100">
          <div class="row">
            <div class="col-xl-12 col-lg-12 col-md-12 layout-spacing">
              <b-form id="general-info" novalidate class="section general-info">
                <div class="info">
                  <h6 class="">General Information</h6>
                  <div class="row">
                    <div class="col-lg-11 mx-auto">
                      <div class="row">
                        <div class="col-xl-2 col-lg-12 col-md-4">
                          <div class="upload mt-4 pr-md-4">
                            <input ref="fl_profile" type="file" class="d-none" accept="image/*" @change="change_file" />
                            <img :src="selected_file ? selected_file : 'http://127.0.0.1:8000' + form.imageU" alt="profile" class="profile-preview" @click="$refs.fl_profile.click()" />
                            <p class="mt-2">Upload Picture</p>
                          </div>
                        </div>
                        <div class="col-xl-10 col-lg-12 col-md-8 mt-md-0 mt-4">
                          <div class="form">
                            <div class="row">
                              <div class="col-sm-6">
                                <div class="form-group">
                                  <label>First Name</label>
                                  <b-input
                                    class="mb-4"
                                    type="text"
                                    placeholder="First Name"
                                    v-model="form.firstname"
                                    :class="[is_submit_form1 ? (form.firstname && form.firstname != 0 ? 'is-valid' : 'is-invalid') : '']"
                                  ></b-input>
                                  <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                                  <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.firstname }">First Name field cannot be empty</b-form-invalid-feedback>
                                </div>
                              </div>
                              <div class="col-sm-6">
                                <div class="form-group">
                                  <label>Last Name</label>
                                  <b-input class="mb-4" type="text" placeholder="Last Name" v-model="form.lastname" :class="[is_submit_form1 ? (form.lastname && form.lastname.length!=0 ? 'is-valid' : 'is-invalid') : '']"></b-input>
                                  <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.lastname }">Last Name field cannot be empty</b-form-invalid-feedback>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </b-form>
            </div>

            <div class="col-xl-12 col-lg-12 col-md-12 layout-spacing">
              <b-form id="about" class="section about">
                <div class="info">
                  <h5 class="">About</h5>
                  <div class="row">
                    <div class="col-md-11 mx-auto">
                      <div class="form-group">
                        <label for="aboutBio">Bio</label>
                        <b-textarea id="aboutBio" placeholder="Tell something interesting about yourself" rows="10" v-model="form.bio"> </b-textarea>
                      </div>
                    </div>
                  </div>
                </div>
              </b-form>
            </div>

            <div class="col-xl-12 col-lg-12 col-md-12 layout-spacing">
              <b-form id="contact" class="section contact">
                <div class="info">
                  <h5 class="">Contact</h5>
                  <div class="row">
                    <div class="col-md-11 mx-auto">
                      <div class="row">
                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="country">Country</label>
                            <country-select class="country-select" v-model="form.country" />
                          </div>
                        </div>
                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="address">Address</label>
                            <b-input class="mb-4" type="text" placeholder="Address" v-model="form.address"></b-input>
                          </div>
                        </div>

                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="phone">Phone</label>
                            <b-input class="mb-4" type="text" placeholder="Write your phone number here" v-model="form.tel" :class="[is_submit_form1 ? (form.tel && form.tel.length!=0  ? 'is-valid' : 'is-invalid') : '']"></b-input>
                            <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.tel }">Phone Number cannot be empty</b-form-invalid-feedback>
                          </div>
                        </div>
                        <!--<div class="col-md-6">
                          <div class="form-group">
                            <label for="email">Email</label>
                            <b-input class="mb-4" type="email" placeholder="Write your email here" v-model="form.email"></b-input>
                          </div>
                        </div>-->
                      </div>
                    </div>
                  </div>
                </div>
              </b-form>
            </div>
          </div>
        </div>
      </div>

      <div class="account-settings-footer">
        <div class="as-footer-container">
          <b-button variant="primary" @click="Reset()">Reset All</b-button>
          <b-button variant="success" @click="updateProfile()">Save Changes</b-button>

          <b-toast id="message" header-class="d-none" body-class="toast-success d-flex justify-content-between" toaster="b-toaster-top-right"> Settings Saved Successfully </b-toast>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import '@/assets/sass/scrollspyNav.scss';
import '@/assets/sass/users/account-setting.scss';
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';
export default {
  metaInfo: { title: 'Account Setting' },
  data() {
    return {
      selected_file: null,
      form: {
        lastname: '',
        firstname: '',
        address: '',
        country: '',
        email: '',
        tel: '',
      },
      CurrentUser: [],
      userprofile: [],
      reset: [],
      is_submit_form1: false,
    };
  },
  computed: {
    ...mapGetters({
      User: 'StateUser',
      Users: 'StateUsers',
      Userprofiles: 'StateUserprofiles',
    }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
  },
  created: function () {
    this.GetUsers();
    this.GetUserprofiles();

    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }

    axios.get('/userprofile/userprofile-detail/' + this.$route.params.id + '/').then((response) => {
      this.form = response.data;
      this.reset = response.data;
      console.log(this.reset);
    });
  },
  mounted() {},
  methods: {
    change_file(event) {
      this.selected_file = event.target.files[0];
    },
    updateProfile() {
      try {
        this.is_submit_form1 = true;
        if (this.form.firstname && this.form.firstname.length != 0 && this.form.lastname && this.form.lastname.length != 0 && this.form.tel && this.form.tel.length!=0) {
          var formdata = new FormData();
          if (this.selected_file != null) {
            formdata.append('imageU', this.selected_file);
          }
          formdata.append('lastname', this.form.lastname);
          formdata.append('firstname', this.form.firstname);
          formdata.append('address', this.form.address);
          formdata.append('email', this.form.email);
          formdata.append('bio', this.form.bio);
          formdata.append('tel', this.form.tel);
          axios.put('/userprofile/userprofile-update/' + this.$route.params.id + '/', formdata);
          this.GetUserprofiles();
          this.$router.push('/profile/' + this.form.id);
        }
      } catch (error) {
        throw 'Il ya un error!';
      }
    },
    Reset() {
      this.form.firstname = this.reset.firstname;
      this.form.lastname = this.reset.lastname;
      this.form.bio = this.reset.bio;
      this.form.address = this.reset.address;
      this.form.email = this.reset.email;
      this.form.tel = this.reset.tel;
    },
    ...mapActions(['GetUsers', 'GetUserprofiles']),
  },
};
</script>
