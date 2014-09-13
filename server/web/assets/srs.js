
        var srs_player = null;
        var url = 'rtmp://192.168.1.233:1935/live/stream1';;
        
        var __active_dar = null;
        function select_dar(dar_id, num, den) {
            srs_player.set_dar(num, den);
            
            if (__active_dar) {
				__active_dar.removeClass("btn--primary");
                __active_dar.addClass("btn--secondary");
            }
            
            __active_dar = $(dar_id);
            __active_dar.removeClass("btn--secondary");
			__active_dar.addClass("btn--primary");
        }
        
        var __active_size = null;
        function select_fs_size(size_id, refer, percent) {
            srs_player.set_fs(refer, percent);
            
            if (__active_size) {
				__active_size.removeClass("btn--primary");
                __active_size.addClass("btn--secondary");
            }
            
            __active_size = $(size_id);
            __active_size.addClass("active");
            __active_size.removeClass("btn--secondary");
			__active_size.addClass("btn--primary");
        }
        
        var __active_bt = null;
        function select_buffer_time(bt_id, buffer_time) {
            srs_player.set_bt(buffer_time);
            
            if (__active_bt) {
				__active_bt.removeClass("btn--primary");
                __active_bt.addClass("btn--secondary");
            }
            
            __active_bt = $(bt_id);
            __active_bt.addClass("active");
            __active_bt.removeClass("btn--secondary");
			__active_bt.addClass("btn--primary");
        }
        
        $(function(){
            // get the vhost and port to set the default url.
            // for example: http://192.168.1.213/players/jwplayer6.html?port=1935&vhost=demo
            // url set to: rtmp://demo:1935/live/livestream
            srs_init("#txt_url", null, "#main_modal");
            
            $("#rtmp").val(url);
                if (srs_player) {
                    return;
                }
                
                $("#div_container").remove();
                
                var div_container = $("<div/>");
                $(div_container).attr("id", "div_container");
                $("#player").append(div_container);
                
                var player = $("<div/>");
                $(player).attr("id", "player_id");
                $(div_container).append(player);
                
                srs_player = new SrsPlayer("player_id", srs_get_player_width(), srs_get_player_height());
                srs_player.on_player_ready = function() {
                    select_buffer_time("#btn_bt_0_8", 0.8);
                    this.play(url);
                };
                srs_player.on_player_metadata = function(metadata) {
                    $("#btn_dar_original").text("Original " + "(" + metadata.width + ":" + metadata.height + ")");
                    select_dar("#btn_dar_original", 0, 0);
                    select_fs_size("#btn_fs_size_screen_100", "screen", 100);
                };
                srs_player.on_player_timer = function(time, buffer_length) {
                    var buffer = buffer_length / this.buffer_time * 100;
                    $("#pb_buffer").width(Number(buffer).toFixed(1) + "%");
                    
                    $("#pb_buffer").text("Buffer Length:" + Number(buffer_length).toFixed(3) + "s(" 
                        + Number(buffer).toFixed(3) + "%)");
                    
                    var time_str = "";
                    // day
                    time_str = padding(parseInt(time / 24 / 3600), 2, '0') + " ";
                    // hour
                    time = time % (24 * 3600);
                    time_str += padding(parseInt(time / 3600), 2, '0') + ":";
                    // minute
                    time = time % (3600);
                    time_str += padding(parseInt(time / 60), 2, '0') + ":";
                    // seconds
                    time = time % (60);
                    time_str += padding(parseInt(time), 2, '0');
                    // show
                    $("#txt_time").val(time_str);
                };
                srs_player.start();
            
            
          
            url = 'rtmp://192.168.1.233:1935/live/stream1';
            
            $("#btn_pause").click(function(){
                if ($("#btn_pause").text() == "Pause") {
                    $("#btn_pause").text("Resume");
                    srs_player.pause();
                } else {
                    $("#btn_pause").text("Pause");
                    srs_player.resume();
                }
            });
            
            if (true) {
                $("#btn_dar_original").click(function(){
                    select_dar("#btn_dar_original", 0, 0);
                });
                $("#btn_dar_21_9").click(function(){
                    select_dar("#btn_dar_21_9", 21, 9);
                });
                $("#btn_dar_16_10").click(function(){
                    select_dar("#btn_dar_16_10", 16, 10);
                });
                $("#btn_dar_16_9").click(function(){
                    select_dar("#btn_dar_16_9", 16, 9);
                });
                $("#btn_dar_4_3").click(function(){
                    select_dar("#btn_dar_4_3", 4, 3);
                });
                $("#btn_dar_1_1").click(function(){
                    select_dar("#btn_dar_1_1", 1, 1);
                });
                $("#btn_dar_fill").click(function(){
                    select_dar("#btn_dar_fill", -1, -1);
                });
            }
            
            if (true) {
                $("#btn_fs_size_video_100").click(function(){
                    select_fs_size("#btn_fs_size_video_100", "video", 100);
                });
                $("#btn_fs_size_video_75").click(function(){
                    select_fs_size("#btn_fs_size_video_75", "video", 75);
                });
                $("#btn_fs_size_video_50").click(function(){
                    select_fs_size("#btn_fs_size_video_50", "video", 50);
                });
                $("#btn_fs_size_screen_100").click(function(){
                    select_fs_size("#btn_fs_size_screen_100", "screen", 100);
                });
                $("#btn_fs_size_screen_75").click(function(){
                    select_fs_size("#btn_fs_size_screen_75", "screen", 75);
                });
                $("#btn_fs_size_screen_50").click(function(){
                    select_fs_size("#btn_fs_size_screen_50", "screen", 50);
                });
            }
            
            if (true) {
                $("#btn_bt_0_5").click(function(){
                    select_buffer_time("#btn_bt_0_5", 0.5);
                });
                $("#btn_bt_0_8").click(function(){
                    select_buffer_time("#btn_bt_0_8", 0.8);
                });
                $("#btn_bt_1").click(function(){
                    select_buffer_time("#btn_bt_1", 1);
                });
                $("#btn_bt_2").click(function(){
                    select_buffer_time("#btn_bt_2", 2);
                });
                $("#btn_bt_3").click(function(){
                    select_buffer_time("#btn_bt_3", 3);
                });
                $("#btn_bt_5").click(function(){
                    select_buffer_time("#btn_bt_5", 5);
                });
                $("#btn_bt_10").click(function(){
                    select_buffer_time("#btn_bt_10", 10);
                });
                $("#btn_bt_15").click(function(){
                    select_buffer_time("#btn_bt_15", 15);
                });
                $("#btn_bt_20").click(function(){
                    select_buffer_time("#btn_bt_20", 20);
                });
                $("#btn_bt_30").click(function(){
                    select_buffer_time("#btn_bt_30", 30);
                });
            }
        });