<template>
  <div class="col-xl-12 col-lg-12 col-md-12 mb-4 mt-4 float-container">
    <b-card class="b-l-card-1">
      <div
        class="float-right bg-danger ml-2 del"
        style="border-radius: 50px; padding: 5px"
        v-if="(CurrentUserProfile.id == service.userprofileS && service.userprofileS != null) || (CurrentUserEntreprise.id == service.userentrepriseS && service.userentrepriseS != null)"
      >
        <a @click="deleteService(service.id, index)"
          ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="18" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 22 24">
            <path
              fill="currentColor"
              d="M16.313 4V2.144C16.313.96 15.353 0 14.169 0H7.831A2.142 2.142 0 0 0 5.69 2.189v-.002V4H0v2h.575c.196.023.372.099.515.214l-.002-.002c.119.157.203.346.239.552l.001.008l1.187 15.106c.094 1.84.094 2.118 2.25 2.118h12.462c2.16 0 2.16-.275 2.25-2.113l1.187-15.1c.036-.217.12-.409.242-.572l-.002.003a.994.994 0 0 1 .508-.212h.58v-2h-5.687zM7 2.187c0-.6.487-.938 1.106-.938h5.734c.618 0 1.162.344 1.162.938V4h-8zM6.469 20l-.64-12h1.269l.656 12zm5.225 0H10.32V8h1.375zm3.85 0h-1.275l.656-12h1.269z"
            />
          </svg>
        </a>
      </div>
      <div
        class="float-right bg-warning"
        style="border-radius: 100px; padding: 5px"
        v-if="(CurrentUserProfile.id == service.userprofileS && service.userprofileS != null) || (CurrentUserEntreprise.id == service.userentrepriseS && service.userentrepriseS != null)"
      >
        <a :href="'/updateservice/' + service.id"
          ><svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="feather feather-edit-3"
          >
            <path d="M12 20h9"></path>
            <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
          </svg>
        </a>
      </div>
      <div
        class="float-right bg-success mr-2"
        v-b-modal.promotion
        style="border-radius: 10px; padding: 5px"
        v-if="
          ((CurrentUserProfile.id == service.userprofileS && service.userprofileS != null) || (CurrentUserEntreprise.id == service.userentrepriseS && service.userentrepriseS != null)) &&
          promoted == false
        "
      >
        Promote
        <b-modal id="promotion" title="Promote your service !" centered>
          <label>Number of days</label>
          <b-input placeholder="1,3,7..etc" type="number" v-model="nbDays" min="1" value="7"></b-input>
          <template #modal-footer>
            <b-button variant="primary" @click="promote()">Submit your promotion</b-button>
          </template>
        </b-modal>
      </div>
      <div v-if="service.promoted == true" class="float-right mr-1" style="border-radius: 5px; padding: 5px">
        <b-badge variant="success"> Promoted Service</b-badge>
      </div>
      <div class="float-child">
        <img :src=" service.imageS" class="img-fluid img-thumbnail mt-4" style="height: 450px; width: 100%" />
      </div>
      <div class="float-child">
        <strong class="card-category ml-4">
          <b-badge variant="warning"> {{ type.descT }} </b-badge></strong
        >
        <h4 class="card-title mt-4 ml-4">{{ service.titleS }}</h4>
        <p class="card-text meta-info meta-time mb-4 ml-4">
          <small class="">{{ service.dateS | formatDate }}</small>
        </p>
        <p class="card-text mb-2 ml-4">{{ service.details }}</p>
        <div class="w-50">
          <span v-if="service.userprofileS != CurrentUserProfile.id || service.userentrepriseS != CurrentUserEntreprise.id">
            <span v-if="isLoggedIn && existprofile == true || existentreprise == true">
              <span v-b-modal.Rating>
                <div class="d-flex col-xl-12 col-lg-12 col-md-12 mt-4 mb-4 ">
                  <div class="text-center mt-3">
                    
                    <span class="h1 font-weight-bolder mr-1">{{ average }}</span
                    ><br />
                    <span class="p">out of 5</span>
                  </div>
                  <div class="flex-grow-1">
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb5" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb4" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        >
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb3" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb2" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb1" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                  </div>
                </div>
              </span>
            </span>
            <span v-else>
              <a href="/auth/login">
                 <div class="d-flex col-xl-12 col-lg-12 col-md-12 mt-4 mb-4 ">
                  <div class="text-center mt-3">
                    <span class="h1 font-weight-bolder mr-1">{{ average | formatNumber}}</span
                    ><br />
                    <span class="p">out of 5</span>
                  </div>
                  <div class="flex-grow-1">
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb5" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb4" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        >
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb3" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb2" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb1" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                  </div>
                </div>
              </a>
            </span>
          </span>
          <span v-else>
            <span @click="showAlert()">
              <div class="d-flex col-xl-12 col-lg-12 col-md-12 mt-4 mb-4 ml-4">
                  <div class="text-center mt-3">
                    <span class="h1 font-weight-bolder mr-1">{{ average }}</span
                    ><br />
                    <span class="p">out of 5</span>
                  </div>
                  <div class="flex-grow-1">
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb5" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          />
                        </svg>
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb4" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        >
                      </div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb3" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg
                        ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb2" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                    <div class="row">
                      <div class="col-lg-6 text-right"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.5em" height="0.5em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1024 1024">
                          <path
                            fill="currentColor"
                            d="m908.1 353.1l-253.9-36.9L540.7 86.1c-3.1-6.3-8.2-11.4-14.5-14.5c-15.8-7.8-35-1.3-42.9 14.5L369.8 316.2l-253.9 36.9c-7 1-13.4 4.3-18.3 9.3a32.05 32.05 0 0 0 .6 45.3l183.7 179.1l-43.4 252.9a31.95 31.95 0 0 0 46.4 33.7L512 754l227.1 119.4c6.2 3.3 13.4 4.4 20.3 3.2c17.4-3 29.1-19.5 26.1-36.9l-43.4-252.9l183.7-179.1c5-4.9 8.3-11.3 9.3-18.3c2.7-17.5-9.5-33.7-27-36.3z"
                          /></svg></div>
                      <div class="col-6 mt-2">
                        <b-progress variant="gradient-warning" :value="nb1" :min="0" :max="nbTotal" class="br-30 progress-sm"></b-progress>
                      </div>
                    </div>
                  </div>
                </div>
            </span>
          </span>
        </div>
        <h6 class="mb-4 ml-4">
          <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 100 100">
            <path
              fill="currentColor"
              d="M88.286 67.965c-.022-.038-.052-.069-.076-.105l.002-.001L61.307 21.26l-.015.008a2.08 2.08 0 0 0-.929-.801l.038-.022l-7.986-4.612l8.871 15.365l20.178 34.949l-.002.001c.024.036.054.067.076.105a2.091 2.091 0 0 1-.765 2.855l.014.025l-29.861 17.24l1.293 2.239c.026.055.044.112.075.166a2.085 2.085 0 0 0 2.772.801l.005.008l32.465-18.743l-.014-.025a2.09 2.09 0 0 0 .764-2.854z"
            />
            <path
              fill="currentColor"
              d="M73.88 67.143a2.091 2.091 0 0 0 .765-2.855c-.022-.038-.052-.069-.076-.105l.002-.001l-26.905-46.599l-.015.008a2.08 2.08 0 0 0-.929-.801l.038-.022l-11.01-6.357v.044a2.082 2.082 0 0 0-1.846-.107l-.012-.021l-.206.119c-.004.003-.009.003-.013.006s-.007.006-.012.008L12.478 22.69a2.078 2.078 0 0 0-1.037 1.764l-.007-.004v12.714l.021-.012c-.047.427.03.872.261 1.273c.014.024.032.042.047.065l26.815 46.446c.026.055.044.112.075.166a2.085 2.085 0 0 0 2.772.801l.005.008l32.465-18.743l-.015-.025zM29.545 27.522a3.865 3.865 0 1 1 1.415-5.279a3.862 3.862 0 0 1-1.415 5.279z"
            />
          </svg>
          : <b-badge variant="success"> {{ service.priceS }} $ </b-badge>
        </h6>
        <h6 class="card-text mb-4 ml-4">
          <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32">
            <path
              fill="currentColor"
              d="M16 2A11.013 11.013 0 0 0 5 13a10.889 10.889 0 0 0 2.216 6.6s.3.395.349.452L16 30l8.439-9.953c.044-.053.345-.447.345-.447l.001-.003A10.885 10.885 0 0 0 27 13A11.013 11.013 0 0 0 16 2Zm0 15a4 4 0 1 1 4-4a4.005 4.005 0 0 1-4 4Z"
            />
            <circle cx="16" cy="13" r="4" fill="none" />
          </svg>
          : {{ service.addressS }}
        </h6>
        <h6 class="card-text mb-4 ml-4">
          <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 20 20">
            <path
              fill="currentColor"
              d="M19 14.5v-9c0-.83-.67-1.5-1.5-1.5H3.49c-.83 0-1.5.67-1.5 1.5v9c0 .83.67 1.5 1.5 1.5H17.5c.83 0 1.5-.67 1.5-1.5zm-1.31-9.11c.33.33.15.67-.03.84L13.6 9.95l3.9 4.06c.12.14.2.36.06.51c-.13.16-.43.15-.56.05l-4.37-3.73l-2.14 1.95l-2.13-1.95l-4.37 3.73c-.13.1-.43.11-.56-.05c-.14-.15-.06-.37.06-.51l3.9-4.06l-4.06-3.72c-.18-.17-.36-.51-.03-.84s.67-.17.95.07l6.24 5.04l6.25-5.04c.28-.24.62-.4.95-.07z"
            />
          </svg>
          : <a :href="'mailto:' + service.email" target="_blank"> {{ service.email }} </a>
        </h6>
        <h6 class="card-text mb-4 ml-4">
          <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32">
            <path
              fill="currentColor"
              d="m20.33 21.48l2.24-2.24a2.19 2.19 0 0 1 2.34-.48l2.73 1.09a2.18 2.18 0 0 1 1.36 2v5A2.17 2.17 0 0 1 26.72 29C7.59 27.81 3.73 11.61 3 5.41A2.17 2.17 0 0 1 5.17 3H10a2.16 2.16 0 0 1 2 1.36l1.09 2.73a2.16 2.16 0 0 1-.47 2.34l-2.24 2.24s1.29 8.73 9.95 9.81Z"
            />
          </svg>
          : {{ service.contactS }}
        </h6>
        <h6 class="card-text mb-4 ml-4">
          <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
            <path
              fill="currentColor"
              d="M213.3 384c0-87 65.2-158.7 149.3-169.2v-1.5c5.5-8 21.3-21.3 21.3-42.7s-21.3-42.7-21.3-53.3C362.7 32 319.2 0 256 0c-60.5 0-106.7 32-106.7 117.3c0 10.7-21.3 32-21.3 53.3s15.2 35.4 21.3 42.7c0 0 0 21.3 10.7 53.3c0 10.7 21.3 21.3 32 32c0 10.7 0 21.3-10.7 42.7L64 362.7C21.3 373.3 0 448 0 512h271.4c-35.5-31.3-58.1-77-58.1-128zM384 256c-70.7 0-128 57.3-128 128s57.3 128 128 128s128-57.3 128-128s-57.3-128-128-128zm85.3 149.3h-64v64h-42.7v-64h-64v-42.7h64v-64h42.7v64h64v42.7z"
            />
          </svg>
          :
          <span v-if="service.userprofileS != null">
            <span v-for="u in Userprofiles" :key="u.id">
              <span v-if="u.id == service.userprofileS">
                <router-link :to="'/profile/' + u.id"> {{ u.firstname }} {{ u.lastname }} </router-link>
              </span>
            </span>
          </span>
          <span v-if="service.userentrepriseS != null">
            <span v-for="e in Userentreprises" :key="e.id">
              <span v-if="e.id == service.userentrepriseS">
                <router-link :to="'/entreprisedetails/' + e.id"> {{ e.nameE }} </router-link>
              </span>
            </span>
          </span>
        </h6>
      </div>
    </b-card>

    <b-modal id="Rating" :title="'Rate ' + service.titleS" centered>
      <b-form-rating id="rating" v-model="nbEval" precision="2" show-value-max show-value variant="warning" size="lg" class="mb-2 bg-transparent border-0"> </b-form-rating>
       <label >Your feedback </label>
                    <b-form-group class="mb-3">
                      <b-input type="text" placeholder="Feedback " v-model="commentEval" ></b-input>
                    </b-form-group>
      <template #modal-footer>
        <b-button variant="primary" @click="rating()">Submit your rating</b-button>
      </template>
    </b-modal>
    <div class="row layout-top-spacing mt-5">
      <div id="custom_carousel" class="col-lg-12 layout-spacing">
        <div class="panel-body style-custom-1">
          <div class="container" style="max-width: 928px">
            <div class="row">
              <h3 class="text-center mb-4">Related Services</h3>
              <div class="col-lg-12 col-md-12 p-0">
                <b-carousel ref="carousel1" :interval="2000" controls indicators class="style-custom-1">
                  <span v-for="s in Services" :key="s.id">
                    <span v-if="s.accepted == true && s.id != service.id">
                      <b-carousel-slide>
                        <template #img>
                          <a :href="'/servicedetails/' + s.id">
                            <img class="d-block w-100 slide-image" height="350px" :src=" s.imageS" alt="First slide" />
                          </a>
                        </template>

                        <h3>
                          <b-badge variant="warning">{{ s.titleS }}</b-badge>
                        </h3>
                      </b-carousel-slide>
                    </span>
                  </span>
                </b-carousel>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import '@/assets/sass/components/custom-carousel.scss';
import axios from 'axios';
import { mapGetters, mapActions } from 'vuex';
export default {
  metaInfo: { title: 'Service Details' },
  data() {
    return {
      service: [],
      userprofile: [],
      userentreprise: [],
      type: [],
      CurrentUser: [],
      CurrentUserProfile: [],
      CurrentUserEntreprise: [],
      existprofile: false,
      existentreprise: false,
      average: 0,
      nbDays: 7,
      promoted: false,
      commentEval:'',
      nbEval: null,
      Evaluation: [],
      nb1: 0,
      nb2: 0,
      nb3: 0,
      nb4: 0,
      nb5: 0,
      nbTotal: 0,
    };
  },
  mounted: {
    Evaluations() {
      this.GetEvaluations();
    },
  },
  created: function () {
    this.GetUserprofiles();
    this.GetServicetypes();
    this.GetServices();
    this.GetUsers();
    this.GetEvaluations();
    this.GetServicepromotions();
    this.GetUserentreprises();
    this.totalEval = this.Evaluations.length;
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let u in this.Userprofiles) {
      if (this.Userprofiles[u].userU == this.CurrentUser.id) {
        this.CurrentUserProfile = this.Userprofiles[u];
        this.existprofile = true;
      }
    }
    for (let ue in this.Userentreprises) {
      if (this.Userentreprises[ue].userE == this.CurrentUser.id) {
        this.CurrentUserEntreprise = this.Userentreprises[ue];
        this.existentreprise = true;
      }
    }
    axios.get('/service/service-detail/' + this.$route.params.id + '/').then((response) => {
      this.service = response.data;
      if (this.service.accepted == false) {
        this.$router.push('/services');
      }
      for (let u in this.Userprofiles) {
        if (this.Userprofiles[u].id == this.service.userprofileS) {
          this.userprofile = this.Userprofiles[u];
        }
      }
      for (let ue in this.Userentreprises) {
        if (this.Userentreprises[ue].id == this.service.userentrepriseS) {
          this.userentreprise = this.Userentreprises[ue];
        }
      }
      for (let s in this.Servicepromotions) {
        if (this.Servicepromotions[s].serviceP == this.service.id) {
          this.promoted = true;
          const d = new Date(this.Servicepromotions[s].dateP);
          d.setDate(d.getDate() + parseInt(this.Servicepromotions[s].nbDays));
          if (new Date() > d && this.Servicepromotions[s].dateP != null) {
            axios.delete(`https://cargeeks.herokuapp.com/servicepromotion/servicepromotion-delete/${this.Servicepromotions[s].id}/`);
            axios.post('/service/service-update/' + this.service.id + '/', { promoted: false, accepted: this.service.accepted });
            this.promoted = false;
            this.$router.go();
          }
        }
      }
      for (let ev in this.Evaluations) {
        if (this.Evaluations[ev].serviceEval == this.service.id && this.Evaluations[ev].nbEval == 5) {
          this.nb5++;
        } else if (this.Evaluations[ev].serviceEval == this.service.id && this.Evaluations[ev].nbEval == 4) {
          this.nb4++;
        } else if (this.Evaluations[ev].serviceEval == this.service.id && this.Evaluations[ev].nbEval == 3) {
          this.nb3++;
        } else if (this.Evaluations[ev].serviceEval == this.service.id && this.Evaluations[ev].nbEval == 2) {
          this.nb2++;
        } else if (this.Evaluations[ev].serviceEval == this.service.id && this.Evaluations[ev].nbEval == 1) {
          this.nb1++;
        }
      }
      this.nbTotal = this.nb1 + this.nb2 + this.nb3 + this.nb4 + this.nb5;
      for (let t in this.Servicetypes) {
        if (this.Servicetypes[t].id == this.service.typeS) {
          this.type = this.Servicetypes[t];
        }
      }
      var sum = 0;
      var nb = 0;
      for (let e in this.Evaluations) {
        if (this.Evaluations[e].serviceEval == this.service.id) {
          sum += this.Evaluations[e].nbEval;
          nb++;
        }
      }
      this.average = sum / nb;
      axios.post('/service/service-update/' + this.service.id + '/', {
        nbvisits: this.service.nbvisits + 1,
        nbEval: this.average,
      });
    });
  },
  methods: {
    ...mapActions(['GetUserentreprises', 'CreateNotification', 'GetServicepromotions', 'GetServices', 'GetUserprofiles', 'CreateServicepromotion', 'GetServicetypes', 'GetUsers', 'GetEvaluations']),
    promote() {
      if(this.CurrentUser.is_superuser==false){
      this.CreateServicepromotion({ serviceP: this.service.id, nbDays: this.nbDays });
      this.CreateNotification({message:' requested a Promotion on their service !',byuserprofileNo:this.CurrentUserProfile.id,foradmin:true})
      this.$swal('Good Job!', 'Your Service promotion has been sent, Please wait for the administrator to launch your promotion !', 'success');
    }else if(this.CurrentUser.is_superuser==true){
      const current = new Date();
      this.CreateServicepromotion({ serviceP: this.service.id, nbDays: this.nbDays,Running: true , dateP:current.getFullYear()+'-'+(current.getMonth()+1)+'-'+current.getDate() });
      axios.post('/service/service-update/' + this.service.id + '/', { promoted: true });
      }
      this.promoted = true;
      this.CreateNotification({message:' requested a Promotion on their service !',byuserprofileNo:this.CurrentUserProfile.id,foradmin:true})
      this.$swal('Good Job!', 'Your Service promotion has been sent, Please wait for the administrator to launch your promotion !', 'success');
    },
    deleteService(id) {
      this.$swal({
        icon: 'warning',
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        showCancelButton: true,
        confirmButtonText: 'Delete',
        padding: '2em',
      }).then((result) => {
        if (result.value) {
          axios.delete(`https://cargeeks.herokuapp.com/service/service-delete/${id}/`);
          this.$swal('Deleted!', 'Your Service has been deleted.', 'success');
          this.$router.push('/services');
        }
      });
    },

    async rating() {
      let done = false;
      if (this.Evaluations.length == 0) {
        axios.post('/evaluation/evaluation-create/', {
          userEval: this.CurrentUser.id,
          serviceEval: this.service.id,
          nbEval: this.nbEval,
          commentEval:this.commentEval
        });
      } else {
        for (let e in this.Evaluations) {
          if (this.Evaluations[e].userEval == this.CurrentUser.id && this.Evaluations[e].serviceEval == this.service.id) {
            axios.post('/evaluation/evaluation-update/' + this.Evaluations[e].id + '/', {
              nbEval: this.nbEval,
            });

            done = true;
            this.GetEvaluations();
          }
        }
        if (done == false) {
          axios.post('/evaluation/evaluation-create/', {
            userEval: this.CurrentUser.id,
            serviceEval: this.service.id,
            nbEval: this.nbEval,
            commentEval:this.commentEval
          });

          this.GetEvaluations();
        }
        this.GetEvaluations();
      }
      this.CreateNotification({ message: ' Rated your Service ' + this.nbEval + ' Stars !',byuserprofileNo:this.CurrentUserProfile.id,byuserentrepriseNo:this.CurrentUserEntreprise.id,userprofileNo:this.service.userprofileS,entrepriseNo:this.service.userentrepriseS, serviceNo: this.service.id });
      this.$bvModal.hide('Rating');
      this.$router.go();
    },
    async showAlert() {
      this.$swal({
        title: 'You cannot rate your service',
        padding: '2em',
      });
    },
    /* async showAlert1() {
      this.$swal({
        title: 'You cannot rate this service as an entreprise',
        padding: '2em',
      });
    },*/
  },
  computed: {
    ...mapGetters({
      Userentreprises: 'StateUserentreprises',
      Userprofiles: 'StateUserprofiles',
      Servicetypes: 'StateServicetypes',
      User: 'StateUser',
      Users: 'StateUsers',
      Evaluations: 'StateEvaluations',
      Servicepromotions: 'StateServicepromotions',
      Services: 'StateServices',
    }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
    postRating: function () {
      return this.service.nbEval;
    },
  },
};
</script>

<style scoped>
.float-container {
  padding: 10px;
}

.float-child {
  width: 50%;
  float: left;
  padding: 10px;
}
.del {
  cursor: pointer;
}
</style>>
