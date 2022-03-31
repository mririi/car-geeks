import axios from 'axios'
import { setStore, getStore } from '@/config/utils'
const user = getStore('user')

const state = {
  loginUser: user,
  //USERS
  user: null,
  users:null,
  userprofiles:null,
  evaluationprofile:null,
  evaluationentreprises:null,
  userentreprises:null,
  entreprisepromotions:null,
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
  servicepromotions:null,
  //OTHERS
  reclamations:null,
  preferences:null,
  isEntreprise:null,
  notifications:null,
  countryList:[],
  chats:null,
  groups:null,
  groupmembers:null,
  groupposts:null,
};

const getters = {
  getLoginUserInfo(state) {
    return state.loginUser
  },
  //USERS
  StateCountrylist: (state) => state.countryList,
  isAuthenticated: (state) => !!state.user,
  StateUser: (state) => state.user,
  StateRoles: (state) => state.roles,
  StateUsers: (state) => state.users,
  StateUserprofiles: (state) => state.userprofiles,
  StateUserentreprises: (state) => state.userentreprises,
  StateisEntreprise: (state) => state.isEntreprise,
  StateEntreprisepromotions: (state) => state.entreprisepromotions,
  StateEvaluationProfile:(state) => state.evaluationprofile,
  StateEvaluationentreprises:(state) => state.evaluationentreprises,

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
  StateServicepromotions:(state) => state.servicepromotions,
  //OTHERS
  StatePreferences: (state) => state.preferences,
  StateReclamations: (state) => state.reclamations,
  StateNotifications:(state) => state.notifications,
  StateChats:(state) => state.chats,
  StateGroups:(state) => state.groups,
  StateGroupMember:(state) => state.groupmembers,
  StateGroupposts:(state) => state.groupposts,
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
  async GetEntreprisepromotions({ commit }) {
    let response = await axios.get("entreprisepromotion/entreprisepromotion-list/");
    commit("setEntreprisepromotions", response.data);
  },
  async GetUsers({ commit }) {
    let response = await axios.get("user/users/");
    commit("setUsers", response.data);
  },
  async CreateUserprofile({ dispatch }, profile) {
    await axios.post("/userprofile/userprofile-create/", profile);
    return await dispatch("GetUserprofiles");
  },
  async CreateUserentreprise({ dispatch }, profile) {
    await axios.post("/userentreprise/userentreprise-create/", profile);
    return await dispatch("GetUserentreprises");
  },
  async CreateEntreprisepromotion({ dispatch }, entreprise) {
    await axios.post("/entreprisepromotion/entreprisepromotion-create/", entreprise);
    return await dispatch("GetServicepromotions");
  },
  async GetUserprofiles({ commit }) {
    let response = await axios.get("userprofile/userprofile-list/");
    commit("setUserprofiles", response.data);
  },
  async GetEvaluationProfile({ commit }) {
    let response = await axios.get("evaluationprofile/evaluationprofile-list/");
    commit("setEvaluationProfile", response.data);
  },
  async GetEvaluationentreprises({ commit }) {
    let response = await axios.get("evaluationentreprise/evaluationentreprise-list/");
    commit("setEvaluationentreprises", response.data);
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
  async CreateService({ dispatch }, service) {
    await axios.post("/service/service-create/", service);
    return await dispatch("GetServices");
  },
  async CreateServicetype({ dispatch }, servicetype) {
    await axios.post("/servicetype/servicetype-create/", servicetype);
    return await dispatch("GetServicetypes");
  },
  async GetServicetypes({ commit }) {
    let response = await axios.get("servicetype/servicetype-list/");
    commit("setServicetypes", response.data);
  },
  async CreateServicepromotion({ dispatch }, servicepro) {
    await axios.post("/servicepromotion/servicepromotion-create/", servicepro);
    return await dispatch("GetServicepromotions");
  },
  async GetServicepromotions({ commit }) {
    let response = await axios.get("servicepromotion/servicepromotion-list/");
    commit("setServicepromotions", response.data);
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
  async CreateNotification({ dispatch }, notification) {
    await axios.post("/notifications/notification-create/", notification);
    return await dispatch("GetNotifications");
  },
  async CreateChat({ dispatch }, chat) {
    await axios.post("/chat/chat-create/", chat);
    return await dispatch("GetChats");
  },
  async GetReclamations({ commit }) {
    let response = await axios.get("reclamation/reclamation-list/");
    commit("setReclamations", response.data);
  },
  async GetNotifications({ commit }) {
    let response = await axios.get("notification/notification-list/");
    commit("setNotifications", response.data);
  },
  async GetChats({ commit }) {
    let response = await axios.get("chat/chat-list/");
    commit("setChats", response.data);
  },
  async GetGroups({ commit }) {
    let response = await axios.get("group/group-list/");
    commit("setGroups", response.data);
  },
  async GetGroupmembers({ commit }) {
    let response = await axios.get("groupmember/groupmember-list/");
    commit("setGroupmembers", response.data);
  },
  async GetGroupposts({ commit }) {
    let response = await axios.get("postgroup/postgroup-list/");
    commit("setGroupposts", response.data);
  },
  async CreateGrouppost({ dispatch }, group) {
    await axios.post("/postgroup/postgroup-create/", group);
    return await dispatch("GetGroupposts");
  },
  async CreateGroup({ dispatch }, group) {
    await axios.post("/group/group-create/", group);
    return await dispatch("GetGroups");
  },
  async CreateGroupmember({ dispatch }, groupmember) {
    await axios.post("/groupmember/groupmember-create/", groupmember);
    return await dispatch("GetGroupmembers");
  },
};

const mutations = {
  setLoginUser(state, user) {
    state.loginUser = user
    state.user=user.google.user.username
    setStore('user', user)
    
  },
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
  setEntreprisepromotions(state, entreprisepromotions) {
    state.entreprisepromotions = entreprisepromotions;
  },
 setEvaluationProfile(state,evaluationprofile)
 {
 state.evaluationprofile=evaluationprofile;
 },
 setEvaluationentreprises(state,evaluationentreprise)
 {
 state.evaluationentreprises=evaluationentreprise;
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
  setServicepromotions(state, servicepromotions) {
    state.servicepromotions = servicepromotions;
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
  setChats(state,chats)
  {
      state.chats=chats;
  },
  setGroups(state,groups)
  {
      state.groups=groups;
  },
  setGroupmembers(state,groupmembers)
  {
      state.groupmembers=groupmembers;
  },
  setGroupposts(state,groupposts)
  {
      state.groupposts=groupposts;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
}
