
<template>
  <div class="about">
    <p>{{ message }}</p>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h1>アカウント</h1>
    <v-simple-table>
      <thead></thead>
      <tbody>
        <tr>
          <th>アカウントID</th>
          <td>{{ account.id }}</td>
        </tr>
        <tr>
          <th>アカウント名称</th>
          <td>{{ account.account_name }}</td>
        </tr>
        <tr>
          <th>有効開始日</th>
          <td>{{ account.start_on }}</td>
        </tr>
        <tr>
          <th>有効終了日</th>
          <td>{{ account.end_on }}</td>
        </tr>
        <tr>
          <th>作成者</th>
          <td>{{ account.created_by }}</td>
        </tr>
        <tr>
          <th>作成日時</th>
          <td>{{ account.created_at }}</td>
        </tr>
        <tr>
          <th>更新者</th>
          <td>{{ account.updated_by }}</td>
        </tr>
        <tr>
          <th>更新日時</th>
          <td>{{ account.updated_at }}</td>
        </tr>
        <tr>
          <th>ステータス</th>
          <td>{{ account.status }}</td>
        </tr>
        <tr></tr>
      </tbody>
    </v-simple-table>
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
		status: 0
	}

export default {
  name: "SS",
  data() {
    return {
      account: account,
      message: "出力メッセージ",
    };
  },
};
</script>
