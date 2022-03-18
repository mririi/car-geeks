<template>
    <div class="layout-px-spacing">
        <portal to="breadcrumb">
            <ul class="navbar-nav flex-row">
                <li>
                    <div class="page-header">
                        <nav class="breadcrumb-one" aria-label="breadcrumb">
                            <ol class="breadcrumb">
                                <li class="breadcrumb-item active" aria-current="page"><span>Entreprise Portfolio</span></li>
                            </ol>
                        </nav>
                    </div>
                </li>
            </ul>
        </portal>

        <div class="row layout-top-spacing">
            <div class="col-xl-12 col-lg-12 col-md-12 col-12 layout-spacing">
                <div class="panel br-4">
                    <div class="panel-body">
                      <b-media>
                        <div class=" float-right bg-success mr-2"  v-b-modal.promotion style="border-radius: 10px; padding: 5px" v-if="CurrentUserEntreprise.id == userentreprise.id && promoted==false">
                        Promote
                      <b-modal id="promotion" title="Promote your service !" centered>
                        <label>Number of days</label>
                        <b-input placeholder="1,3,7..etc" type="number" v-model="nbDays" min=1 value="7"></b-input>
                        <template #modal-footer>
                      <b-button variant="primary" @click="promote()">Submit your promotion request</b-button>
                    </template>
                      </b-modal>
                    </div>
                        <template #aside>
                          <div v-if="CurrentUser.id == userentreprise.userE">
                <a :href="'/updateentreprise/'+userentreprise.id" style="border-radius: 15px; padding:5px" class="btn-warning">Modify Portfolio</a>
                      </div>
                        </template>
                      </b-media>
                      <h1 class="text-center mt-1 mb-5">Portfolio {{userentreprise.typeE}} </h1>
                      <b-media>
                        <template #aside>
                          <img :src="'http://127.0.0.1:8000'+userentreprise.imageE" class="img-fluid img-thumbnail w-75 mh-75"  />
                        </template>
                       <h1 style="margin-top:200px"> {{userentreprise.nameE}}</h1>
                      </b-media>
                      <b-media right-align class="mt-5 ">
                        
                        <template #aside>
                          <svg xmlns="http://www.w3.org/2000/svg"  aria-hidden="true" role="img" width="600px" height="600px" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path fill="currentColor" d="M19.43 12.98c.04-.32.07-.64.07-.98s-.03-.66-.07-.98l2.11-1.65c.19-.15.24-.42.12-.64l-2-3.46c-.12-.22-.39-.3-.61-.22l-2.49 1c-.52-.4-1.08-.73-1.69-.98l-.38-2.65C14.46 2.18 14.25 2 14 2h-4c-.25 0-.46.18-.49.42l-.38 2.65c-.61.25-1.17.59-1.69.98l-2.49-1c-.23-.09-.49 0-.61.22l-2 3.46c-.13.22-.07.49.12.64l2.11 1.65c-.04.32-.07.65-.07.98s.03.66.07.98l-2.11 1.65c-.19.15-.24.42-.12.64l2 3.46c.12.22.39.3.61.22l2.49-1c.52.4 1.08.73 1.69.98l.38 2.65c.03.24.24.42.49.42h4c.25 0 .46-.18.49-.42l.38-2.65c.61-.25 1.17-.59 1.69-.98l2.49 1c.23.09.49 0 .61-.22l2-3.46c.12-.22.07-.49-.12-.64l-2.11-1.65zM12 15.5c-1.93 0-3.5-1.57-3.5-3.5s1.57-3.5 3.5-3.5s3.5 1.57 3.5 3.5s-1.57 3.5-3.5 3.5z"><animateTransform attributeName="transform" attributeType="XML" dur="10s" from="0 12 12" repeatCount="indefinite" to="360 12 12" type="rotate"/></path></svg>
                        </template>
                        <h1 style="margin-top:40%;margin-left:28%;color:#25d5e4"> What we do?</h1>
                        <h2 style="margin-left:30%"> {{userentreprise.typeE}}</h2>
                       
                      </b-media>
                      <b-media class="">
                        <template #aside>
                          <svg xmlns="http://www.w3.org/2000/svg" style="margin-left:30%" aria-hidden="true" role="img" width="500px" height="500px" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><path fill="currentColor" d="M5.933.87a2.89 2.89 0 0 1 4.134 0l.622.638l.89-.011a2.89 2.89 0 0 1 2.924 2.924l-.01.89l.636.622a2.89 2.89 0 0 1 0 4.134l-.637.622l.011.89a2.89 2.89 0 0 1-2.924 2.924l-.89-.01l-.622.636a2.89 2.89 0 0 1-4.134 0l-.622-.637l-.89.011a2.89 2.89 0 0 1-2.924-2.924l.01-.89l-.636-.622a2.89 2.89 0 0 1 0-4.134l.637-.622l-.011-.89a2.89 2.89 0 0 1 2.924-2.924l.89.01l.622-.636zM7.002 11a1 1 0 1 0 2 0a1 1 0 0 0-2 0zm1.602-2.027c.04-.534.198-.815.846-1.26c.674-.475 1.05-1.09 1.05-1.986c0-1.325-.92-2.227-2.262-2.227c-1.02 0-1.792.492-2.1 1.29A1.71 1.71 0 0 0 6 5.48c0 .393.203.64.545.64c.272 0 .455-.147.564-.51c.158-.592.525-.915 1.074-.915c.61 0 1.03.446 1.03 1.084c0 .563-.208.885-.822 1.325c-.619.433-.926.914-.926 1.64v.111c0 .428.208.745.585.745c.336 0 .504-.24.554-.627z"/></svg>
                        </template>
                        <h1 style="margin-top:20%;margin-left:28%;color:#25d5e4"> What are we?</h1>
                       <h5 style="margin-left:15%"> {{userentreprise.bio}}</h5>
                      </b-media>
                      <b-media right-align class="mt-5 ">
                        
                        <template #aside>
                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="500px" height="500px" preserveAspectRatio="xMidYMid meet" viewBox="0 0 100 100"><path fill="currentColor" d="M2 12a2.5 2.5 0 0 0-2.5 2.5v71A2.5 2.5 0 0 0 2 88h66.88c-.874-1.15-1.746-2.301-2.624-3.45c-1.092-1.611-2.678-2.99-3.143-4.948c-6.43 2.654-13.818 2.9-20.416.697c-.145-.047-.287-.105-.431-.154c-.757.74-1.573 2.03-1.702 2.855h-9.507c.714-2.419-.802-6.196.632-8.658c.114-.03.252-.223.315-.422c-.162-.152-.326-.3-.484-.455c-1.406.428-1.968 1.487-2.75 2.416c.427 2.024-2.655 1.545-2.344 3.61c2.147 1.665-1.982.396-3.21.529c-1.303.014-5.115-1.35-3.792 1.44c-.207.766-.016 1.236.365 1.54h-.584c-.091-.876-1.741-1.006-2.377-1.436c-1.071-.26-2.35-.39-3.459-.884c-.285.792-2.857 1.698-3.42 2.32H4.5V46.469c.767.514 2.487.31.143-.8H4.5V34.155c.455-.23.78-.303.76.082c1.127-.38 1.618-3.123 3.568-2c1.216.179 3.228 2.064 2.217 2.3c.788 1.924 1.347.685 2.314 2.978c-.662 3.136 1.873 5.46 3.264 7.459c1.666.692 2.325 2.846 5.033 2.93c.368.322.84.614 1.332.894c.135-1.034.326-2.06.567-3.074c-.065-.015-.128-.024-.198-.047c-2.605 2.403-3.139-1.757-.595-1.92c.17-.011.353-.002.55.025c.295-.035.54 0 .747.073a28.893 28.893 0 0 1 3.673-7.713a27.8 27.8 0 0 1 2.883-3.612c-.526-.88-1.064-1.371-1.699-.222c-.048-1.705-4.658-3.492-1.266-1.856c1.779 1.533 2.362-.266 2.643-1.494c1.525-1.59-1.563-2.133-1-3.172c-.936-1.403-2.322-2.84-3.746-3.709c-2.762.32-3.73-.263-.037-.265c.333-1.725.886-2.947 1.267-4.399c-.4-.115-.818-.097-1.23-.098c-1.767-.237-2.816.446-2.78 1.795c-1.327-.106-.135-2.368-2.181-1.677c-3.102-.049.648.999.36 1.15c-.355.796-2.59.3-2.327 1.107c-1.024-1.894-1.49.903-2.287-1.013c-.48-.46 2.01.454 1.443-1.223c-1.254-.48-1.703.36-2.68.703c-2.916 1.614.509 3.132 1.99 3.67c2.232-.595 2.23-1.347 3.782-.52c1.74.965-1.757.287-1.65 1.772c-.2-.923-.45-1.48-1.53-.297c-1.44.26-2.083-1.719-3.158-1.58c-2.45-.333-1.535 5.177.483 3.301c1.221 2.113-1.56.554-2.385.318c-1.863 2.081-3.87-.054-6.094-.14c-.712-.474-1.41-.48-2.033-.239V17h26.223c-1.87.051-3.54.298-2.86 1.643c-.11 2.594 3.246.534 3.729 2.88c1.394 1.639-.829 5.124 1.582 4.512c-.887 1.079-.776 2.798-.084 4.153a29.788 29.788 0 0 1 8.588-5.036c.055-.308.012-.662-.172-1.08c-.313-1.569 1.143-2.07.633-3.81c.686-1.31.154-2.696-1.022-3.262H95.5v7.078a3.817 3.817 0 0 0-.477-.168c-1.409 1.277-.27 1.398.477 1.111v1.116c-1.666-.937-3.496-1.04-5.273-.65c-.807-1.403-3.664-1.37-4.604-2.633c-1.656-1.984.505-1.392 1.95-1.545c-.41-1.24-2.87-1.828-3.909-1.623c-1.877 1.028.986 1.95.697 3.33c0 1.003-1.223 1.01-2.29.955c.431-1.062-2.043-2.368-3.024-1.504c-1.857-.562-2.565-.232-1.34-2.166c-.428-1.487-2.197-1.515-2.99-2.547c-1.013 2.148-2.702 1.497-4.512 2.805c-.725 1.06-2.235 2.012-2.31 2.712c-1.122.527-2.245-2.162-3.032.22c-.714 2.016.04 2.993-2.369 1.343c-2.493-2.657 5.008-4.933 2.22-6.064c-2.314.675-3.705 2.306-4.165 4.623c-.249.527-.136.894.127 1.191c8.784 2.62 16.053 9.684 19.008 18.35c.046-.522.133-1.024.308-1.391c.739-.564.153 2.165 1.68.613c-1.125 2.415 2.828.32 3.363-.677c-.784-1.968 2.82-2.895 2.736-3.266c-1.327-1.392-.573-.007-2.037.312c-.485-.646.93-4.188-.953-3.863c-2.812-.724 2.392-2.795 3.797-2.033c.64-2.368 1.56-.482-.021.607c-.602 2.101-.314 4.967 1.457 2.159c.796-.775.598-2.795 1.634-3.147c1.392-.656 3.876-1.169 3.811-3.197c.014-.004.027-.003.041-.006V83h-3.959c.858-1.188 1.993-3.22.791-3.957c-1.811-.313-3.164-2.497-5.353-2.406c-.988-1.138-3.263-1.714-3.875-1.936c-.612-.222-1.674 1.061-2.762.494a2.782 2.782 0 0 0-.987.018c3.274 4.25 6.517 8.523 9.772 12.787H98a2.5 2.5 0 0 0 2.5-2.5v-71A2.5 2.5 0 0 0 98 12Zm48.69 5.32c-1.61.793 1.245 3.95 1.324.936c.295.44 2.274.884 1.627-.535c-1.438-.847-1.22.127-2.952-.4zm23.081.002c-1.737.846 1.52.862 0 0zm-55.18.287c-1.3.966 1.908 1.922.17.051zm10.645.573c.325.312-.321.201 0 0zM16.68 19.418c.153.177-.08.013 0 0zm4.453.412c1.567.272-.12.64 0 0zm2.195.18c1.49-.095.547.37 0 0zm-4.375.066c.969.1-.124.449 0 0zm3.102 1.408c.98.226-.482.305 0 0zm.691 1.559c-.59 1.882 2.097 4.43.012 2.285c-.573-.858-.871-1.68-.012-2.285zm-3.498.19c.859 1.435 2.167 1.818 1.072 2.312c-.727-.352-.895-1.449-1.072-2.313zm13.479 1.447c.121.081-.326.02 0 0zm-20.276.453c-.112.454-.155.007 0 0zm7.744.734c-.07.946-.457-.017 0 0zm5.748.006c-.374 1.85 1.11 1.732 1.01 1.918c-1.226.54-.933 2.764-1.871 1.067c-.592-.276.304-2.718.707-2.932zm-6.027.002c.131.03-.009.433 0 0zm72.336.166c.04.068-.174.17 0 0zm-72.264.242c.682.714-.914.65 0 0zm31.778.983a25.156 25.156 0 0 0-15.082 5.154c-11.09 8.445-13.248 24.365-4.803 35.455c7.905 10.381 22.34 12.885 33.25 6.238l2.084 2.737c-.41.954-.372 1.866.105 2.494l15.12 19.855c.9 1.181 3.073 1.04 4.853-.316c1.78-1.355 2.493-3.412 1.594-4.594l-15.12-19.855c-.478-.628-1.347-.908-2.376-.766l-2.084-2.736c9.309-8.75 10.736-23.33 2.832-33.711c-4.223-5.545-10.315-8.855-16.737-9.725a25.538 25.538 0 0 0-3.636-.23zm-28.389 2.508c.625 1.484 3.039.613 2.094 2.636c1.052.99-.167 4.48-.576 1.506c-2.618-.013-3.868-2.625-1.67-3.996zm2.281.246c.8.68-1.26.379 0 0zm62.828 1.828c.07-.05.244.309 0 0zm-35.713 1.021a19.62 19.62 0 0 1 14.893 7.76a19.635 19.635 0 0 1-3.734 27.576a19.635 19.635 0 0 1-27.577-3.734a19.635 19.635 0 0 1 3.735-27.576a19.613 19.613 0 0 1 12.683-4.026zm38.588 1.03c-1.57 1.299 1.885 1.061 0 0zm1.87 1.082c-1.738.849 1.519.85 0 0zm1.132.396c-1.55 1.29 1.58.612 0 0zm-.062.28c.086-.001-.053.091 0 0zm.148.161c.047.076-.125.016 0 0zM52.11 36.86c-2.186-.039-4.344.45-6.334 1.328c.104.127.253.249.471.359c-2-.65-2.582 1.877-1.74 3.014l1.353.111l1.131-.498c.731-.76.913-.629 1.149-1.78l.441.057l.35-.146l.797.394c.956.374 1.001 1.18.681 1.416c-.453.279.081.32.125.493c.226-.065.358-.26.5-.364l.256-.092c.934-.613.282-.815-.367-1.642l.344.088c.503.57.799 1.215 1.097 1.9c.034.027.065.062.104.074c.226.075.545.05.818-.025c.27-.074.288-.589.242-1.082c.385 1.756 4.161 1.234 1.914 2.305c-1.295.029-3.353-.681-3.732.216c-.838-.38-1.266-.629-1.436-.824c-.516-.194-2.001-.756-2.054-.756c-.063 0-1.953.344-1.953.344l-1.56.592c-.507 1.634-1.307.76-1.579 2.027c-.213.81-2.046 2.56-1.086 3.938c.857 3.986 5.826 1.332 6.984 3.246c-.544 1.179 2.147 3.422.641 5.353c.71 2.805 2.618 7.494 5.688 3.502c.81-2.39 2.554-3.682 2.492-6.053c-.927-2.335 4.53-4.066 2.347-5.957c-.523.062-.583.175-.998.313c-.872-.033-1.097-.736-1.394-1.178a7.397 7.397 0 0 1-.6-1.017c.555.86 1.128 1.59 1.932 2.039c1.391-.312 2.986-1.341 3.635-2.096c-.016-2.943 3.94.11 3.86 2.322c.245.596.556 1.01.868 1.252a15.07 15.07 0 0 0-1.254-4.086c-1.109-2.434-2.885-4.524-5.043-6.088c-.04.062-.14.066-.12-.084a16.46 16.46 0 0 0-.895-.591c.033.139.073.28.119.423c-.131-.195-.269-.393-.383-.584c-2.356-1.388-5.058-2.184-7.81-2.164zm32.537.132c.725 2.066-2.522 6.854-2.994 3.711c.333-1.554 2.998-1.319 2.994-3.71zm-60.875.545c.146-.017-.023.075 0 0zm1.541.727c.291.242-.352.182 0 0zm30.028.066c.807.68 3.283 1.58.662.862c-1.364.623-1.786.224-.662-.862zm-6.238 1.21c-.176.054-.027.419-.137.534c.75.367.33-.347.441-.464c-.152-.072-.246-.089-.304-.07zm11.433.745c.232.603.386.988-.21.24a.41.41 0 0 0 .21-.24zm-11.363.075c-.294-.032-.45.165-.451.44c.775.421.695-.274.79-.327a.982.982 0 0 0-.34-.113zm11.974 4.283c.442.018-.423.64-.275.035c.123-.027.212-.038.275-.035zm30.461 3.912c-1.44 1.53 1.716 1.799 0 0zm-.1.238c.148-.016-.027.102 0 0zm.124.219c.014.103-.15-.025 0 0zm1.047.2c-1.395 1.214 1.684.772 0 0zm.15.345c.106-.018-.02.147 0 0zm-.197.053c.092.124-.081.07 0 0zm-11.397 1.572c.025.624.03 1.247.016 1.87c1.147.183 2.584.131 2.611 1.4c2.056.089-.212 3.092-.287.312a4.049 4.049 0 0 0-2.443.414a30.065 30.065 0 0 1-1.332 6.42c1.68-.533 3.394-.481 4.406 1.152c2.665-.01.398 1.807 2.287 2.178c.805-1.644-.424-1.437 1.086-2.777c1.465-1.873.506-4.292-.955-5.315c-.304-1.158-1.515-1.784-.945-2.574c1.11 1.505 2.683.378 1.37-.436c.969-.905 4.431 2.332 2.487-.158c-.96-.178-2.279-2.163-2.578-.885c-.086 1.06-2.731-1.609-3.707-.517c-.282-.984-1.662-.39-1.74.049c.424-.66.157-1.001-.276-1.133zm5.088.855c-1.433.814 1.294.786 0 0zm-37.435.07c.115.26-.033.043 0 0zm-12.553.122a15.73 15.73 0 0 0 .459 4.123c1.15-1.742 1.105-3.378-.459-4.123zm49.914.048c.086.062-.106.024 0 0zm.969.12c.467.33-.468.33 0 0zm0 .01c-.426.306.425.306 0 0zm-.873.087c.016.101-.148-.018 0 0zm-5.102 1.086c-.01.24-.031.48-.047.72c.323-.364.463-.74.047-.72zM58.45 54.617c-1.156.635 1.237.925.237.18l-.043-.107zm1.352.178c-1.142.714-2.914 4.118-.457 4.225c.592-.704 2.093-3.843.457-4.225zm30.976 2.168c-.915 1.805 2.657 1.083 0 0zm-29.146.24c-1.486.997 1.441.871 0 0zm31.531 4.116c.846 1.915-1.96 3.062-1.748 4.84c1.44.694 2.183-1.918 3.197-2.717c1.199-1.048-.944-1.358-1.449-2.123zm-66.508 5.89c.164 1.054.658 2.074 1.54 2.385a29.368 29.368 0 0 1-1.54-2.385z" color="currentColor"/></svg>                        </template>
                        <h1 style="margin-top:25%;margin-left:28%;color:#25d5e4"> Where are we?</h1>
                        <h2 style="margin-left:35%">In  {{userentreprise.country}}, {{userentreprise.addressE}}</h2>   
                      </b-media>
                      <b-media class="mt-5 ">
                        
                        <template #aside>
                    <svg xmlns="http://www.w3.org/2000/svg" class="mr-5" aria-hidden="true" role="img" width="500px" height="500px" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path fill="currentColor" d="M21 2H6a2 2 0 0 0-2 2v3H2v2h2v2H2v2h2v2H2v2h2v3a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1V3a1 1 0 0 0-1-1zm-8 2.999c1.648 0 3 1.351 3 3A3.012 3.012 0 0 1 13 11c-1.647 0-3-1.353-3-3.001c0-1.649 1.353-3 3-3zM19 18H7v-.75c0-2.219 2.705-4.5 6-4.5s6 2.281 6 4.5V18z"/></svg>
                        </template>
                        <h1 style="margin-top:25%;margin-left:24%;color:#25d5e4"> How to contact us?</h1>
                        <h2 style=";margin-left:34%"> <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path fill="currentColor" d="M24 13h-2a3.003 3.003 0 0 0-3-3V8a5.006 5.006 0 0 1 5 5Z"/><path fill="currentColor" d="M28 13h-2a7.008 7.008 0 0 0-7-7V4a9.01 9.01 0 0 1 9 9zm-7.667 8.482l2.24-2.24a2.167 2.167 0 0 1 2.337-.48l2.728 1.092A2.167 2.167 0 0 1 29 21.866v4.961a2.167 2.167 0 0 1-2.284 2.169C7.594 27.806 3.732 11.61 3.015 5.408A2.162 2.162 0 0 1 5.169 3h4.873a2.167 2.167 0 0 1 2.012 1.362l1.091 2.728a2.167 2.167 0 0 1-.48 2.337l-2.24 2.24s1.242 8.732 9.908 9.815z"/></svg> {{userentreprise.contactE}}</h2>
                        <h4 style="margin-top:3%;margin-left:34%"><a :href="'mailto:' + user.email" target="_blank"
                            ><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="2em" height="2em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><path fill="currentColor" d="M4 3a2 2 0 0 0-2 2v.201l6 3.231l6-3.23V5a2 2 0 0 0-2-2H4Zm10 3.337L8.237 9.44a.5.5 0 0 1-.474 0L2 6.337V11a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V6.337Z"/></svg> {{user.email}}
                        </a>
                        </h4>
                       
                      </b-media>
                     <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 layout-spacing">
      <div class="widget widget-recent-orders">
        <div class="widget-heading">
          <h5>Other Entreprises</h5>
          <div class="row mr-1 float-right">
            <div class="col-lg-12 col-md-12 col-sm-12 filtered-list-search-live mx-auto">
              <b-form class="form-inline my-2 my-lg-0 justify-content-center" @submit.prevent="search">
                <div class="w-100">
                  <b-input v-model="search" class="w-100 product-search br-25" placeholder="Search Entreprises" @keyup="search"></b-input>
                </div>
              </b-form>
            </div>
          </div>
        </div>
        <div class="widget-content">
          <b-table-simple responsive>
            <b-thead>
              <b-tr>
                <b-th><div class="th-content">Entreprise</div></b-th>
                <b-th><div class="th-content">Business type</div></b-th>
                <b-th><div class="th-content">Email</div></b-th>
                <b-th><div class="th-content">Phone</div></b-th>
                <b-th><div class="th-content th-heading">Country</div></b-th>
                <b-th><div class="th-content">Address</div></b-th>
              </b-tr>
            </b-thead>

            <b-tbody>
              <b-tr v-for="e in filteredList" :key="e.id">
                <b-td
                  ><a :href="'/entreprisedetails/' + e.id"
                    ><div class="td-content">
                      <img :src="'http://127.0.0.1:8000' + e.imageE" alt="avatar" /><span>{{e.nameE}} </span>
                    </div></a
                  ></b-td
                >
                <b-td
                  ><div class="td-content">
                    <span>{{ e.typeE }}</span>
                  </div></b-td
                >
                <b-td>
                  <div v-for="user in Users" :key="user.id">
                    <div v-if="user.id == e.userE" class="td-content text-primary">{{ user.email }}</div>
                  </div>
                </b-td>
                <b-td
                  ><div class="td-content">{{ e.contactE }}</div></b-td
                >
                <b-td
                  ><div class="td-content">
                    <span>{{ e.country }}</span>
                  </div></b-td
                >
                <b-td
                  ><div class="td-content">{{ e.addressE }}</div></b-td
                >
              </b-tr>
            </b-tbody>
          </b-table-simple>
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
import '@/assets/sass/scrollspyNav.scss';
import '@/assets/sass/widgets/widgets.scss';
import '@/assets/sass/users/user-profile.scss';
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';
    export default {
        metaInfo: { title: 'Portfolio' },
        data() {
    return {
      CurrentUser: [],
      userentreprise: [],
      CurrentUserEntreprise: [],
      user:[],
      nbEval: '',
      search: '',
      UserEval: '',
      nbDays:0,
      average: 0,
      promoted:false,
      existe:false
    };
  },
        mounted() {},
        computed: {
    ...mapGetters({
      Entreprises: 'StateUserentreprises',
      Entreprisepromotions: 'StateEntreprisepromotions',
      Userentreprises: 'StateUserentreprises',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
    filterByAccepted() {
        return this.Userentreprises.filter((entreprise) => {return entreprise.published==true});
    },
    filteredList() {
      return this.filterByAccepted.filter((entreprise) => {
        return (
          entreprise.nameE.toLowerCase().includes(this.search.toLowerCase()) 
        );
      });
    },
    },
        methods: {    ...mapActions(['GetUsers','GetEntreprisepromotions','CreateEntreprisepromotion', 'GetCars', 'GetUserentreprises', 'GetEvaluations', 'GetEvaluationentreprises']),

promote(){
      this.CreateEntreprisepromotion({entreprisePE:this.userentreprise.id,nbDays:this.nbDays})
      this.promoted=true
    },
},
        created: function () {
    this.GetUsers();
    this.GetUserentreprises();
    this.GetEvaluationentreprises();
    this.GetEntreprisepromotions();
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let p in this.Userentreprises) {
      if (this.Userentreprises[p].userE == this.CurrentUser.id) {
        this.CurrentUserEntreprise = this.Userentreprises[p];
        this.existe=true
      }
    }
    axios.get('/userentreprise/userentreprise-detail/' + this.$route.params.id + '/').then((response) => {
      this.userentreprise = response.data;
      console.log(this.Entreprisepromotions)
      for (let s in this.Entreprisepromotions){
        if(this.Entreprisepromotions[s].entreprisePE==this.userentreprise.id){
          this.promoted=true
          const d = new Date(this.Entreprisepromotions[s].datePE)
          d.setDate(d.getDate() + parseInt(this.Entreprisepromotions[s].nbDays))
          console.log(new Date())
          if(new Date()>new Date(this.Entreprisepromotions[s].datePE)){
            axios.delete(`http://127.0.0.1:8000/entreprisepromotion/entreprisepromotion-delete/${this.Entreprisepromotions[s].id}/`)
            axios.post('/userentreprise/userentreprise-update/' + this.userentreprise.id + '/',{promoted:false,published:this.userentreprise.published})
            this.promoted=false
            this.$router.go()
          }
        }
      }
      /*var sum = 0;
    var nb = 0;
    for (let e in this.EvaluationProfile) {
      if (this.EvaluationProfile[e].userentrepriseEval == this.$route.params.id) {
        sum += this.EvaluationProfile[e].nbEval;
        nb++;
      }
    }
    //this.average = sum / nb;*/

    /*axios.put('/userentreprise/userentreprise-update/' + this.userentreprise.id + '/', {
      nbEvalProfile: this.average,
    });*/
    //this.userentreprise.nbEvalProfile=this.average
    axios.get('/user/users/' + this.userentreprise.userE + '/').then((response) => {
      this.user = response.data;})
    });

    
  },
        
    };
</script>
