/**
 * Created by zhouhenglc on 2023/4/4.
 */

function reqReply(msg){
  var data = {'message': msg};
  my_async_request('/chat/completions', 'POST', data, function(res){
    var r_data = res.data;
    for(var index in r_data.responses){
      sendMessage(r_data.responses[index], true);
    }
  })
}
