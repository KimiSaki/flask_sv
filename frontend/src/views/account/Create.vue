
<template>
  <div class="about">
    <p>{{ message }}</p>
    <h1>アカウント</h1>
    <v-form ref="form" v-model="account" :lazy-validation="lazy">
      <v-simple-table>
        <thead></thead>
        <tbody>
          <tr>
            <th>アカウントID</th>
            <td>
              <v-text-field
                v-model="id"
                label="アカウントID"
                readonly
              ></v-text-field>

            </td>
          </tr>
          <tr>
            <th>アカウント名称</th>
            <td>
              <v-text-field
                v-model="account.account_name"
                :counter="64"
                :rules="nameRules"
                label="アカウント名称"
                required
                @change="$v.select.$touch()"
                @blur="$v.select.$touch()"
              ></v-text-field>
            </td>
          </tr>
          <tr>
            <th>有効開始日</th>
            <td>
              <v-menu v-model="menu" max-width="290px" min-width="290px">
                <!-- ポップアップを追加する要素にv-on="on" -->
                <template v-slot:activator="{ on }">
                  <v-text-field
                    slot="activator"
                    v-model="start_on"
                    label="有効開始日"
                    readonly
                    v-on="on" 
                  ></v-text-field>
                </template>
                <v-date-picker v-model="start_on"></v-date-picker>
              </v-menu>
            </td>
          </tr>
          <tr>
            <th>有効終了日</th>
            <td>
              <v-menu v-model="menu" max-width="290px" min-width="290px">
                <!-- ポップアップを追加する要素にv-on="on" -->
                <template v-slot:activator="{ on }">
                  <v-text-field
                    slot="activator"
                    v-model="end_on"
                    label="有効終了日"
                    readonly
                    v-on="on" 
                  ></v-text-field>
                </template>
                <v-date-picker v-model="end_on"></v-date-picker>
              </v-menu>
            </td>
          </tr>
          <tr>
            <th>作成者</th>
            <td>
              <v-text-field
                v-model="account.created_by"
                :counter="10"
                :rules="nameRules"
                label="作成者"
                required
              ></v-text-field>
            </td>
          </tr>
        </tbody>
      </v-simple-table>
      <v-btn class="mr-4" @click="submit">保存</v-btn>
      <v-btn @click="reset">リセット</v-btn>
    </v-form>
  </div>
</template>
<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

var account = {
  id: 123,
  account_name: "flask_sv_front",
  start_on: "2021/02/01 10:00:00",
  end_on: "2021/11/30 18:00:00",
  created_by: 10,
  created_at: "2021/08/25 12:00:00",
  updated_by: 10,
  updated_at: "2021/08/25 12:00:00",
  status: 0,
};

export default {
  name: "account_create",
  data() {
    return {
      account: account,
      message: "出力メッセージ",
    };
  },
  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
        submit () {
      this.$v.$touch()
    },
    clear () {
      this.$v.$reset()
      this.account_name = ''
      this.start_on = ''
      this.end_on = ''
      this.created_by = ''
    },

  },
};
</script>
