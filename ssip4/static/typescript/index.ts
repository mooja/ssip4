import '../sass/project.sass';

// bootstrap 4 jquery bug
$('.form-group').removeClass('row');

// contact form hiding
$('document').ready(() => {
    $('#contact-us')
        .on('click', e => 
            $('#message-form').toggleClass('d-done'));
    $('.card-body *').css('fontFamily', '"Lato", "sans-serif"');
    $('.card-body *').css('fontSize', "16px");
});

// // upcoming events
// $.ajax({
//     url: 'https://www.googleapis.com/calendar/v3/calendars/me9gs7qmheh6ofpfn294fikmlk@group.calendar.google.com/events',
//     type: 'get',
//     data: {
//         key: 'AIzaSyCXYss3YMn2IJN12Um9hQyzrU6tzwqbP70',
//         singleEvents: true,
//         timeMin: (new Date()).toISOString(),
//         maxResults: 10,
//         orderBy: 'startTime',
//     },
//     success: function(resp) {
//         listUpcomingEvents(resp);
//     }
// });

// function listUpcomingEvents(resp: JQueryXHR): void {
//     var events = resp.items;
//     var uniq_events = {};
//     events.forEach(function(e) {
//         if(!(e.summary in uniq_events))
//             uniq_events[e.summary] = e;
//     });

//     // only show events with unique event titles 
//     events = Object.keys(uniq_events).map(function(k) {
//         return uniq_events[k];
//     });

//     if (events.length > 0) {
//         var events_ul: JQuery<HTMLElement> = $('<ul class="events-list"></li>');
//         for (let i = 0; i < events.length; i++) {
//             var event = events[i];
//             var when = event.start.dateTime;
//             if (!when) {
//                 when = event.start.date;
//             }

//             let event_li = buildEventListItem(event);
//             events_ul.append(event_li);
//         } // end for
//         $('#calendar').append(events_ul);
//     } 
// }


// function buildEventListItem(event) {
//     var sdate = moment(event.start.dateTime);

//     var event_date_month_div: JQuery<HTMLElement> = $('<div class="month">' + sdate.format('MMM') + '</div>');
//     var event_date_date_div: JQuery<HTMLElement> = $('<div class="date">' + sdate.format('D') + '</div>');
//     var event_date_weekday_div: JQuery<HTMLElement> = $('<div class="weekday">' + sdate.format('ddd') + '</div>');
//     var event_date_div: JQuery<HTMLElement> = $('<div class="event-date"></div>');
//     event_date_div.append(event_date_month_div);
//     event_date_div.append(event_date_date_div);
//     event_date_div.append(event_date_weekday_div);

//     var event_description_title: JQuery<HTMLElement> = $('<h3 class="event-title">' + event.summary + '</h3>');
//     var event_description_location: JQuery<HTMLElement> = $('<h4 class="event-location">' + event.location.split(',')[0] + '</h4>');
//     var event_description_time: JQuery<HTMLElement> = $('<h4 class="event-time">' + sdate.format('h:mma') + '</h4>');
//     var event_description_div: JQuery<HTMLElement> = $('<div class="event-description"></div');
//     event_description_div.append(event_description_title);
//     event_description_div.append(event_description_location);
//     event_description_div.append(event_description_time);

//     let event_group_div: JQuery<HTMLElement> = $('<div class="group"></div>');
//     event_group_div.append(event_date_div);
//     event_group_div.append(event_description_div);

//     let event_li: JQuery<HTMLElement> = $('<li></li>');
//     event_li.append(event_group_div);

//     return event_li;
// }
