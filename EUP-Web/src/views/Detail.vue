<template>
    <div>
        <el-descriptions title="Post Information" direction="vertical" :column="4" class="container">
          <el-descriptions-item label="Published_time">{{this.date}}</el-descriptions-item>
          <el-descriptions-item label="Source">
              <el-tag >{{ this.source }}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="label">
              <el-tag type="danger">{{ this.label }}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="spread label">
              <el-tag type="danger">{{ this.label_2 }}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="Content" span=4>{{ this.content }}
          </el-descriptions-item>
          <el-descriptions-item label="Macro media environment" :span="4">
              <el-table
                  :data="macro"
                  style="width: 100%">
                  <el-table-column
                      prop="date"
                      label="date"
                      width="180">
                  </el-table-column>
                  <el-table-column
                      prop="content"
                      label="content">
                  </el-table-column>
              </el-table>
          </el-descriptions-item>
          <el-descriptions-item label="Micro conmunicative environment" :span="4">
              <el-table
                  :data="micro"
                  style="width: 100%">
                  <el-table-column
                      prop="date"
                      label="date"
                      width="180">
                  </el-table-column>
                  <el-table-column
                      prop="content"
                      label="content">
                  </el-table-column>
              </el-table>
          </el-descriptions-item>
          <el-descriptions-item label="Uncertainty Analysis" span="4">
              <el-row>
                  <el-col :span="6">
                      <el-progress type="circle" :percentage="unc" :status="unc > 50 ? 'warning' : 'success'"></el-progress>
                  </el-col>
                  <el-col :span="12">
                      <el-row>
                          <el-col :span="12">
                              macro-media environment uncertainty:
                          </el-col>
                          <el-col :span="6">
                            <el-progress :percentage="macro_unc" :format="format" :status="macro_unc > 60 ? 'warning' : 'success'"></el-progress>
                          </el-col>
                      </el-row>
                      <el-row>
                          <el-col :span="12">
                              micro-communicative environment uncertainty:
                          </el-col>
                          <el-col :span="6">
                            <el-progress :percentage="micro_unc" :format="format" :status="micro_unc > 60 ? 'warning' : 'success'"></el-progress>
                          </el-col>
                      </el-row>
                      <el-row>
                          <el-col :span="12">
                              physical environment uncertainty:
                          </el-col>
                          <el-col :span="6">
                            <el-progress :percentage="physical_unc" :format="format" :status="physical_unc > 60 ? 'warning' : 'success'"></el-progress>
                          </el-col>
                      </el-row>
                      <el-row>
                          <el-col :span="12">
                              message-framing uncertainty:
                          </el-col>
                          <el-col :span="6">
                            <el-progress :percentage="content_unc" :format="format" :status="content_unc > 60 ? 'warning' : 'success'"></el-progress>
                          </el-col>
                      </el-row>
                  </el-col>
              </el-row>
              
          </el-descriptions-item>
      </el-descriptions>
      <div class="center">
        <el-button type="primary"  @click="goBack">Back</el-button>
      </div>
      <div class="filler"></div>
    </div>
  </template>


<script>
import axios from 'axios';
export default {
  data() {
    return {
      id: '1',
      date: '2020-03-23',
      source: 'twitter',
      label: 'fake',
      label_2: 'high',
      content: 'Trump mentions it again, people will be breaking into pet stores. \n\nSales of fish tank additive skyrocket after studies say it could treat coronavirus https://t.co/tlo8fp2k3o via @nypost',
      macro: [{
        date:  '2020-03-23',
        
        content: "Man who tried to treat himself with hydroxychloroquine DIES: Couple ate fish tank cleaner thinking it was the malaria drug that Trump is touting as a miracle coronavirus remedy"
      }, {
        date:  '2020-03-23',
        content: "Covetrus sees surge in online demand for pet products as coronavirus spreads"
      }, {
        date:  '2020-03-23',
        content: "Fish tank treatment uses the same chemical in the drug Trump claims could be a 'game-changer' for treating coronavirus despite zero proof - and prices for it have surged to $500  "
      }, {
        date: '2020-03-20',
        content: "Helena Bonham Carter stocks up on beauty products during outing with her son Billy, 16, and pet dog in London amid COVID-19 pandemic"     
      }, {
        date: '2020-03-23', 
        content: "Amazon BANS sellers shipping non-essential items to its warehouses and will prioritize food, diapers, household cleaning products, and pet and medical supplies as it tries to handle HUGE surge in online orders amid coronavirus panic "
      }],
      micro: [{
        date:  '2020-03-23',
        content: 'RT @RexChapman: While social-distancing this daddy and daughter just caught her first fish.'
      }, {
        date:  '2020-03-22',
        content: 'My fish died from the Corona virus\ud83d\ude14'
      }, {
        date:  '2020-03-23',
        content: "My husband and I tried to take Trump's coronavirus drug - now he is dead: Wife speaks out after they drank fish tank cleaner chloroquine because they mistook it for unproven treatment hydroxychlorquine"
    }],
    macro_unc: 0,
    micro_unc: 0,
    content_unc: 0,
    physical_unc: 0,
    unc: 0,
    }
  },
  created() {
    this.load();
  },
  methods: {
    load(){
      console.log(this.$route.params.id)
      axios.get('/api/getDetail', {
          params: {
            id: this.$route.params.id
        }})
        .then(response => {
          if (response.data.code == 200) {
            console.log(response.data)
            this.id = this.$route.params.id,
            this.date = response.data.data.date,
            this.source = response.data.data.source,
            this.label = response.data.data.label,
            this.label_2 = response.data.data.label_2,
            this.content = response.data.data.content,
            this.macro = response.data.data.macro,
            this.micro = response.data.data.micro
            this.macro_unc = response.data.data.macro_unc;
            this.micro_unc = response.data.data.micro_unc;
            this.content_unc = response.data.data.content_unc;
            this.physical_unc = response.data.data.physical_unc;
            this.unc = (response.data.data.macro_unc + response.data.data.micro_unc + response.data.data.physical_unc + response.data.data.content_unc)/4
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    goBack() {
        this.$router.go(-1); // 返回前一页
    }
  }
}
</script>

<style scoped>
.container {
  margin-top: 40px;
  padding: 0 20px;
}

.container {
  display: flex;
  flex-direction: column;
  height: 100%;
}


.center {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.filler {
  flex: 1;
}
</style>