import Vue from 'vue'
import VueRouter from 'vue-router'

import register from '../components/register.vue' 
import login from '../components/login.vue' 
import info from '../components/info.vue' 

import userinfo from '../components/userinfo.vue' 
import reservation from '../components/reservation.vue' 
import myreservation from '../components/myreservation.vue'
import interview from '../components/interview.vue'

Vue.use(VueRouter)

export default new VueRouter({
	// mode:'history',
	routes:[
		{
			path:"/register",
			name:"register",
			component:register,
		},
		{
			path:"/login",
			name:"login",
			component:login,
		},
		{
			path:"/info",
			name:"info",
			component:info,
			children:[
				{ path: 'userinfo', component: userinfo },
				{ path: 'reservation', component: reservation },
				{ path: 'myreservation', component: myreservation },
        { path:'interview',componet:interview}
          ]
		},
	]
})
