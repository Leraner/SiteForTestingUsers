import { createRouter, createWebHistory } from "vue-router";
import store from "../store";

const routes = [
  // {
  //   path: "/",
  //   name: "Home",
  //   component: () => import("../views/Home.vue"),
  // },
  {
    path: "/profile",
    name: "MyProfile",
    meta: {
      requiredLogin: true,
    },
    component: () => import("../components/Profile/MyProfile.vue"),
  },
  {
    path: "/profile/:username",
    name: "UserProfile",
    props: true,
    component: () => import("../components/Profile/UserProfile.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/Login.vue"),
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("../views/SignUp.vue"),
  },
  {
    path: "/about",
    name: "About",
    component: () => import("../views/About.vue"),
  },
  {
    path: "/tasks",
    name: "Tasks",
    meta: {
      requiredLogin: true,
    },
    component: () => import("../components/Exercise/GetQuestions.vue"),
  },
  {
    path: "/exam/:username/:exam_id",
    name: "UserExam",
    component: () => import("../components/Exam/UserExam.vue"),
    props: true,
    meta: {
      requiredLogin: true,
    },
  },
  {
    path: "/exam/create",
    name: "CreateUserExam",
    component: () => import("../components/Exam/CreateUserExam.vue"),
    meta: {
      requiredLogin: true,
    },
  },
  {
    path: "/",
    name: "Posts",
    component: () => import("../components/Post/PostList.vue")
  },
  {
    path: "/post/:id",
    name: "PostDetail",
    component: () => import("../components/Post/PostDetail.vue"),
    props: true
  },
  {
    path: "/post/create",
    name: "PostCreate",
    component: () => import('../components/Post/PostCreate.vue'),
    meta: {
      requiredLogin: true
    }
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFoundPage",
    component: () => import("../views/NotFoundPage.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requiredLogin) &&
    !store.state.isAuthenticated
  ) {
    next({ name: "Login", query: { to: to.path } });
  } else {
    next();
  }
});

export default router;
