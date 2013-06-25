var currIndex = 0; 
var count = 10;

jQuery(document).ready(function() { 
  getData();
}); 

jQuery(window).scroll(function() { 
  if(jQuery(window).scrollTop() == jQuery(document).height() - jQuery(window).height()) {
    getData();
  }
});

function getData() { 
  jQuery('#loader').show();
  var url = 'json/members/' + currIndex + '/' + count; 
  currIndex += count; 
  jQuery.getJSON(url, function(data) { 
    jQuery.each(data, function(index, val) { 
      addTile(val); 
    });
    $('#loader').hide();
  }); 
}

function addTile(data) {
  console.log(data); 
  var html = '' + 
    '<div class="row-fluid profile-tile">' + 
    '    <div class="span2">' + 
    '      <img src="/static/img/default-avatar.png" width="178" class="avatar">' + 
    '    </div>' + 
    '    <div class="span10">' + 
    '      <h4><a href="#" onclick="return showProfile(' + data.id + ');">' + data.username + '</a></h4>' + 
    '      <div class="row-fluid">' + 
    '        <div class="span12 profile-headline">' + data.headline + '</span>' + 
    '      </div>' + 
    '      <div class="row-fluid">' + 
    '        <div class="span6">' + 
    '          ' + data.age + ' &bull; ' + data.gender + ' &bull; ' + data.relationship_status + '<br />' + 
    '          ' + data.zip_code + 
    '        </div>' + 
    '        <div class="span6">' + 
    '          Last Login: ' + data.last_login + '<br />' + 
    '          Member\'s Engagement: [TBD]' + 
    '        </div>' + 
    '      </div>' + 
    '      <div class="span12 profile-summary">' + 
    '        ' + data.summary +
    '      </div>' + 
    '    </div>' + 
    '  </div>'; 
  jQuery("#posts").append(html);
}

function showProfile(profileID) { 
  var url = 'json/profile/' + profileID; 
  jQuery.getJSON(url, function(data) { 
    console.log(data);
    jQuery('#profile-label').html(data.username);
    jQuery('#profile-headline').html(data.headline);
    jQuery('#profile-summary').html(data.summary);
    jQuery('#profile-stats').html(data.age + " &bull; " + data.gender + 
      " &bull; " + data.relationship_status);
    jQuery('#profile-box').modal({
      //keyboard: false
    }); 
  }); 
  return false; 
}
