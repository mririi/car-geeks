import axios from 'axios'


const state = {
  //USERS
  user: null,
  users:null,
  userprofiles:null,
  userentreprises:null,
  roles:null,
  //QUESTION
  questions: null,
  questioncategories:null,
  replies:null,
  comments:null,
  votes:null,
  //CAR
  cars:null,
  brands:null,
  carenergies:null,
  cartypes:null,
  carmodeles:null,
  carengines:null,
  //SERVICE
  servicetypes:null,
  services:null,
  evaluations:null,
  //OTHERS
  reclamations:null,
  preferences:null,
  isEntreprise:null,
  notifications:null,
  countryList:[],
};

const getters = {
  //USERS
  StateCountrylist: (state) => state.countryList,
  isAuthenticated: (state) => !!state.user,
  StateUser: (state) => state.user,
  StateRoles: (state) => state.roles,
  StateUsers: (state) => state.users,
  StateUserprofiles: (state) => state.userprofiles,
  StateUserentreprises: (state) => state.userentreprises,
  StateisEntreprise: (state) => state.isEntreprise,
  //QUESTION
  StateQuestions: (state) => state.questions,
  StateQuestioncategories: (state) => state.questioncategories,
  StateReplies: (state) => state.replies,
  StateComments: (state) => state.comments,
  StateVotes: (state) => state.votes,
  //CAR
  StateCars: (state) => state.cars,
  StateBrands: (state) => state.brands,
  StateCarenergies: (state) => state.carenergies,
  StateCartypes: (state) => state.cartypes,
  StateCarmodeles: (state) => state.carmodeles,
  StateCarengines: (state) => state.carengines,
  //SERVICE
  StateServices: (state) => state.services,
  StateServicetypes: (state) => state.servicetypes,
  StateEvaluations:(state) => state.evaluations,
  //OTHERS
  StatePreferences: (state) => state.preferences,
  StateReclamations: (state) => state.reclamations,
  StateNotifications:(state) => state.notifications,
};

const actions = {
  //AUTH
  async Register({dispatch}, form) {
    await axios.post('user/users/', form)
    let UserForm = new FormData()
    UserForm.append('username', form.username)
    UserForm.append('password', form.password)
    await dispatch('LogIn', UserForm)
  },
  async LogIn({commit}, user) {
    await axios.post("/auth/", user);
    console.log(user.get("username"))
    await commit("setUser", user.get("username"));
  },
  async LogOut({ commit }) {
    let user = null;
    commit("logout", user);
  },
  //USERS
  async CreateRole({ dispatch }, role) {
    await axios.post("/role/role-create/", role);
    return await dispatch("GetRoles");
  },
  async GetRoles({ commit }) {
    let response = await axios.get("role/role-list/");
    commit("setRoles", response.data);
  },
  async isEntreprise({commit}, is) {
    await commit("setisEntreprise", is);
  },
  async GetUserentreprises({ commit }) {
    let response = await axios.get("userentreprise/userentreprise-list/");
    commit("setUserentreprises", response.data);
  },
  async GetUsers({ commit }) {
    let response = await axios.get("user/users/");
    commit("setUsers", response.data);
  },
  
  async GetUserprofiles({ commit }) {
    let response = await axios.get("userprofile/userprofile-list/");
    commit("setUserprofiles", response.data);
  },
  //QUESTION
  async CreateQuestion({ dispatch }, question) {
    await axios.post("/question/question-create/", question);
    return await dispatch("GetQuestions");
  },
  async GetQuestions({ commit }) {
    let response = await axios.get("question/question-list/");
    commit("setQuestions", response.data);
  },
  async CreateQuestioncategory({ dispatch }, categorie) {
    await axios.post("/questioncategory/questioncategory-create/", categorie);
    return await dispatch("GetQuestioncategories");
  },
  async GetQuestioncategories({ commit }) {
    let response = await axios.get("questioncategory/questioncategory-list/");
    commit("setQuestioncategories", response.data);
  },
  async CreateReply({ dispatch }, reponse) {
    await axios.post("/reply/reply-create/", reponse);
    return await dispatch("GetReplies");
  },
  async GetReplies({ commit }) {
    let response = await axios.get("reply/reply-list/");
    commit("setReplies", response.data);
  },
  async CreateComment({ dispatch }, comment) {
    await axios.post("/comment/comment-create/", comment);
    
    return await dispatch("GetComments");
  },
  async GetComments({ commit }) {
    let response = await axios.get("comment/comment-list/");
    commit("setComments", response.data);
  },
  async CreateVote({ dispatch }, vote) {
    await axios.post("/vote/vote-create/", vote);
    return await dispatch("GetVotes");
  },
  async GetVotes({ commit }) {
    let response = await axios.get("vote/vote-list/");
    commit("setVotes", response.data);
  },
  //CAR
  async CreateCar({ dispatch }, car) {
    await axios.post("/car/car-create/", car);
    return await dispatch("GetCars");
  },
  async GetCars({ commit }) {
    let response = await axios.get("car/car-list/");
    commit("setCars", response.data);
  },
  async CreateBrand({ dispatch }, brand) {
    await axios.post("/brand/brand-create/", brand);
    return await dispatch("GetBrands");
  },
  async GetBrands({ commit }) {
    let response = await axios.get("brand/brand-list/");
    commit("setBrands", response.data);
  },
  async CreateCarmodele({ dispatch }, carmodele) {
    await axios.post("/carmodele/carmodele-create/", carmodele);
    return await dispatch("GetCarmodeles");
  },
  async GetCarmodeles({ commit }) {
    let response = await axios.get("carmodele/carmodele-list/");
    commit("setCarmodeles", response.data);
  },
  async CreateCarengine({ dispatch }, carengine) {
    await axios.post("/carengine/carengine-create/", carengine);
    return await dispatch("GetCarengine");
  },
  async GetCarengines({ commit }) {
    let response = await axios.get("carengine/carengine-list/");
    commit("setCarengines", response.data);
  },
  async CreateCarenergy({ dispatch }, carenergy) {
    await axios.post("/carenergy/carenergy-create/", carenergy);
    return await dispatch("GetCarenergies");
  },
  async GetCarenergies({ commit }) {
    let response = await axios.get("carenergy/carenergy-list/");
    commit("setCarenergies", response.data);
  },
  async CreateCartype({ dispatch }, cartype) {
    await axios.post("/cartype/cartype-create/", cartype);
    return await dispatch("GetCartypes");
  },
  async GetCartypes({ commit }) {
    let response = await axios.get("cartype/cartype-list/");
    commit("setCartypes", response.data);
  },
  //SERVICE
  async GetServices({ commit }) {
    let response = await axios.get("service/service-list/");
    commit("setServices", response.data);
  },
  async CreateServicetype({ dispatch }, servicetype) {
    await axios.post("/servicetype/servicetype-create/", servicetype);
    return await dispatch("GetServicetypes");
  },
  async GetServicetypes({ commit }) {
    let response = await axios.get("servicetype/servicetype-list/");
    commit("setServicetypes", response.data);
  },
  async GetEvaluations({ commit }) {
    let response = await axios.get("evaluation/evaluation-list/");
    commit("setEvaluations", response.data);
  },
  //OTHERS
  async CreatePreference({ dispatch }, preferences) {
    await axios.post("/preferences/preferences-create/", preferences);
    return await dispatch("GetPreferences");
  },
  async GetPreferences({ commit }) {
    let response = await axios.get("preferences/preferences-list/");
    commit("setPreferences", response.data);
  },
  async CreateReclamation({ dispatch }, reclamation) {
    await axios.post("/reclamation/reclamation-create/", reclamation);
    return await dispatch("GetReclamations");
  },
  async GetReclamations({ commit }) {
    let response = await axios.get("reclamation/reclamation-list/");
    commit("setReclamations", response.data);
  },
  async GetNotifications({ commit }) {
    let response = await axios.get("notification/notification-list/");
    commit("setNotifications", response.data);
  },
};

const mutations = {
  //USERS
  setUser(state, username) {
    state.user = username;
  },
  setUsers(state, users) {
    state.users = users;
  },
  setUserprofiles(state, userprofiles) {
    state.userprofiles = userprofiles;
  },
  setUserentreprises(state, userentreprises) {
    state.userentreprises = userentreprises;
  },
  setisEntreprise(state, is) {
    state.isEntreprise = is;
  },
  setRoles(state, roles) {
    state.roles = roles;
  },
  logout(state, user) {
    state.user = user;
  },
  //QUESTION
  setQuestions(state, questions) {
    state.questions = questions;
  },
  setQuestioncategories(state, questioncategories) {
    state.questioncategories = questioncategories;
  },
  setReplies(state, replies) {
    state.replies = replies;
  },
  setComments(state, comments) {
    state.comments = comments;
  },
  setVotes(state, votes) {
    state.votes = votes;
  },
  //CAR
  setCars(state, cars) {
    state.cars = cars;
  },
  setBrands(state, brands) {
    state.brands = brands;
  },
  setCarengines(state, carengines) {
    state.carengines = carengines;
  },
  setCarmodeles(state, carmodeles) {
    state.carmodeles = carmodeles;
  },
  setCartypes(state, cartypes) {
    state.cartypes = cartypes;
  },
  setCarenergies(state, carenergies) {
    state.carenergies = carenergies;
  },
  //SERVICE
  setServices(state, services) {
    state.services = services;
  },
  setServicetypes(state, servicetypes) {
    state.servicetypes = servicetypes;
  },
  setEvaluations(state,evaluations)
  {
      state.evaluations=evaluations;
  },
  //OTHERS
  setPreferences(state, preferences) {
    state.preferences = preferences;
  },
  setReclamations(state, reclamations) {
    state.reclamations = reclamations;
  },
  setNotifications(state,notifications)
  {
      state.notifications=notifications;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
}
