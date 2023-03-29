function sendMessage(message, itsMe) { // ...Mario
  var messageList = document.getElementById("message-list");
  
  var scrollToBottom = (messageList.scrollHeight - messageList.scrollTop - messageList.clientHeight < 80);

  var lastMessage = messageList.children[messageList.children.length-1];
  
  var newMessage = document.createElement("span");
  newMessage.innerHTML = message;

  var className;
  
  if(itsMe)
  {
    className = "me";
    scrollToBottom = true;
  }
  else
  {
    className = "not-me";
  }
  
  if(lastMessage && lastMessage.classList.contains(className))
  {
    lastMessage.appendChild(document.createElement("br"));
    lastMessage.appendChild(newMessage);
  }
  else
  {
    var messageBlock = document.createElement("div");
    messageBlock.classList.add(className);
    messageBlock.appendChild(newMessage);
    messageList.appendChild(messageBlock);
  }
  
  if(scrollToBottom)
    messageList.scrollTop = messageList.scrollHeight;
}

function reqReply(msg){
  var data = {'message': msg};
  my_async_request('/chat/completions', 'POST', data, function(res){
    var r_data = res.data;
    for(var index in r_data.responses){
      sendMessage(r_data.responses[index], true);
    }
  })
}

var message = document.getElementById("message-input");

message.addEventListener("keypress", function(event) {
  var key = event.which || event.keyCode;
  if(key === 13 && this.value.trim() !== "")
  {
    var value = this.value;
    reqReply(value);
    sendMessage(this.value, false);
    this.value = "";
  }
});

$(document).ready(function() {
  reqReply("");
});
