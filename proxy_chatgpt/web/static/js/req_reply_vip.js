/**
 * Created by zhouhenglc on 2023/4/4.
 */
var HISTORY = [];
function reqReply(msg){
  if(msg.length <= 0) {
  }
  else{
    var msg_item = {'role': 'user', 'content': msg};
    HISTORY.push(msg_item);
  }

  var data = {'messages': HISTORY};
  my_async_request('/chat/vip/completions', 'POST', data, function(res){
    var r_data = res.data;
    for(var index in r_data.responses){
      var r_msg = {'role': 'assistant', 'content': r_data.responses[index]};
      HISTORY.push(r_msg);
      sendMessage(r_data.responses[index], true);
    }
  })
}
