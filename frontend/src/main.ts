import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";

import "@/plugins/bootstrap.client.ts";

const app = createApp(App);

app.use(router);

app.mount("#app");
