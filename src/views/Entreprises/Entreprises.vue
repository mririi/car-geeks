<template>
    <div class="layout-px-spacing">
        <portal to="breadcrumb">
            <ul class="navbar-nav flex-row">
                <li>
                    <div class="page-header">
                        <nav class="breadcrumb-one" aria-label="breadcrumb">
                            <ol class="breadcrumb">
                                <li class="breadcrumb-item active" aria-current="page"><span>Entreprises</span></li>
                            </ol>
                        </nav>
                    </div>
                </li>
            </ul>
        </portal>
        <div>
      <div class="mr-1 mt-2 d-flex justify-content-center w-25">
        <div class="col-lg-12 col-md-12 col-sm-12 filtered-list-search-live mx-auto">
          <b-form class="form-inline my-2 my-lg-0 justify-content-center" @submit.prevent="search">
            <div class="w-100">
              <b-input v-model="search" class="w-100 product-search br-25" placeholder="Search Questions" @keyup="search"></b-input>
            </div>
          </b-form>
        </div>
      </div>
    </div>
        <div class="row layout-top-spacing">
            <div class="col-xl-12 col-lg-12 col-md-12 col-12 layout-spacing">
                
                   <div class="fq-article-section">
                    <div class="row">
                        <div v-for="s in filterByPromoted" :key="s.id" class="col-lg-4 col-md-6 mb-lg-0 mb-4 mt-2 text-center">
                          <a v-if="s.published==true"  :href="'/entreprisedetails/'+s.id"> 
                          <b-card class="component-card_4 " style="height:92%">
                            <b-badge class="float-right" variant="danger">Promoted</b-badge>
                            
                                <span class="user-profile ml-5  mt-2">
                                    <img :src="'http://127.0.0.1:8000' + s.imageE" class="col-6" alt="..." />
                                </span>
                                <div class="user-info mt-2 mr-4">
                                    <h5 class="card-user_name">{{s.nameE}}</h5>
                                    <p class="card-user_occupation text-warning">{{s.typeE}}</p>
                                    <div class="card-star_rating">
                                        <span class="badge badge-primary">{{s.nbEval}}</span>
                                    </div>
                                    <b-card-text class="mt-2 text-success"> <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M24 13h-2a3.003 3.003 0 0 0-3-3V8a5.006 5.006 0 0 1 5 5Z"/><path fill="currentColor" d="M28 13h-2a7.008 7.008 0 0 0-7-7V4a9.01 9.01 0 0 1 9 9zm-7.667 8.482l2.24-2.24a2.167 2.167 0 0 1 2.337-.48l2.728 1.092A2.167 2.167 0 0 1 29 21.866v4.961a2.167 2.167 0 0 1-2.284 2.169C7.594 27.806 3.732 11.61 3.015 5.408A2.162 2.162 0 0 1 5.169 3h4.873a2.167 2.167 0 0 1 2.012 1.362l1.091 2.728a2.167 2.167 0 0 1-.48 2.337l-2.24 2.24s1.242 8.732 9.908 9.815z"/></svg> {{s.contactE}} </b-card-text>
                                </div>
                            </b-card>
                            </a>
                            </div>
                            <div v-for="s in filterByNotPromoted" :key="s.id" class="col-lg-4 mb-4 mt-2 text-center">
                          <a v-if="s.published==true" :href="'/entreprisedetails/'+s.id"> 
                          <b-card class="component-card_4" style="height:100%">
                                <span class="user-profile  mt-2" >
                                    <img :src="'http://127.0.0.1:8000' + s.imageE" class="col-6" />
                                </span>
                                <div class="user-info mt-5">
                                    <h5 class="card-user_name">{{s.nameE}}</h5>
                                    <p class="card-user_occupation text-warning">{{s.typeE}}</p>
                                    <div class="card-star_rating">
                                        <span class="badge badge-primary">{{s.nbEval}}</span>
                                    </div>
                                    <b-card-text class="mt-2 text-success"> <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M24 13h-2a3.003 3.003 0 0 0-3-3V8a5.006 5.006 0 0 1 5 5Z"/><path fill="currentColor" d="M28 13h-2a7.008 7.008 0 0 0-7-7V4a9.01 9.01 0 0 1 9 9zm-7.667 8.482l2.24-2.24a2.167 2.167 0 0 1 2.337-.48l2.728 1.092A2.167 2.167 0 0 1 29 21.866v4.961a2.167 2.167 0 0 1-2.284 2.169C7.594 27.806 3.732 11.61 3.015 5.408A2.162 2.162 0 0 1 5.169 3h4.873a2.167 2.167 0 0 1 2.012 1.362l1.091 2.728a2.167 2.167 0 0 1-.48 2.337l-2.24 2.24s1.242 8.732 9.908 9.815z"/></svg> {{s.contactE}} </b-card-text>
                                </div>
                            </b-card>
</a>
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
    .cardzoom:hover{
      zoom:1.05;
    }
</style>
<script>
import '@/assets/sass/pages/faq/faq.scss'
import { mapGetters, mapActions } from 'vuex';
    export default {
        metaInfo: { name: 'Services' },
        data(){
            return{
                search:"",
            }
        },
        mounted() {},
        methods: {
            ...mapActions(['GetUserentreprises','GetEntreprisepromotions', 'GetUsers', 'GetUserprofiles']),
        },
        computed: {
    ...mapGetters({
      Entreprises: 'StateUserentreprises',
      Entreprisepromotions: 'StateEntreprisepromotions',
      Userprofiles: 'StateUserprofiles',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
    filterByAccepted() {
      
        return this.Entreprises.filter((entreprise) => {return entreprise.published==true});
      
    },
    filteredList() {
      return this.filterByAccepted.filter((entreprise) => {
        return entreprise.nameE.toLowerCase().includes(this.search.toLowerCase());
      });
    },
    filterByPromoted: function () {
        return this.filteredList.filter((entreprisep) => {return entreprisep.promoted==true});
    },
    filterByNotPromoted: function () {
        return this.filteredList.filter((entreprisep) => {return entreprisep.promoted==false});
    },
  },
        created: function () {
        this.GetUserentreprises();
        this.GetEntreprisepromotions();
        }
    };
</script>
