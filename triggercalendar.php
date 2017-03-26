<?php

$to = "keerthanamohan19@gmail.com";
// $to = $_POST['email'];
$subject = "Pharmacy- Medication Details";
$message = "Thank you for purchasing from our pharmacy.\r\n\r\n\n";
$location = "Home";
$meeting_duration = 3600;
date_default_timezone_set('America/Halifax');
$currtime = date('Y-m-d H:i:s');
$meetingstamp = STRTOTIME($currtime . "America/Halifax");    
$dtstart= (string)GMDATE("Ymd\THis\Z",$meetingstamp);
echo $dtstart;
$dtend= (string)GMDATE("Ymd\THis\Z",$meetingstamp+$meeting_duration);
echo $dtend;
$todaystamp = GMDATE("Ymd\THis\Z");


//Create Mime Boundry
$mime_boundary = "----Medication Details----".MD5(TIME());
$from_name = "Pharmacist";
$from_address = "mypharmacist@mydomain.com";
//Create Email Headers
$headers = "From: ".$from_name." <".$from_address.">\n";
$headers .= "Reply-To: ".$from_name." <".$from_address.">\n";

$headers .= "MIME-Version: 1.0\n";
$headers .= "Content-Type: multipart/alternative; boundary=\"$mime_boundary\"\n";
$headers .= "Content-class: urn:content-classes:calendarmessage\n";
//==================
$message .= "--$mime_boundary\n";
$message .= "Content-Type: text/html; charset=UTF-8\n";
$message .= "Content-Transfer-Encoding: 8bit\n\n";

$message .= "<html>\n";
$message .= "<body>\n";
$message .= '<img src="https://evisitmydr.com/dev_new/wp-content/uploads/2015/06/patient-icon.png" alt="Prescription details to add to your calendar" />';
$message .= '<p>Dear customer, </p>';
$message .= '<p>Here is the descriptions of medications to be taken. Please click to add it to your calendar event </p>';    
$message .= "</body>\n";
$message .= "</html>\n";
$message .= "--$mime_boundary\n";
$headers .= "MIME-version: 1.0\r\n";
$headers .= "Content-class: urn:content-classes:calendarmessage\r\n";
$headers .= "Content-type: text/calendar; method=REQUEST; charset=UTF-8\r\n";
$message .= 'Content-Type: text/calendar;name="medicationsummary.ics";method=REQUEST\n';
$message .= "Content-Transfer-Encoding: 8bit\n\n";
$message .= "BEGIN:VCALENDAR\r\n\n";
$message .= "VERSION:2.0\r\n\n";
$message .= "PRODID:PHP\r\n\n";
$message .= "METHOD:REQUEST\r\n\n";
$message .= "BEGIN:VEVENT\r\n\n";
$message .= "DTSTART:20170325T010326Z \r\n\n";
$message .= "DTEND:20170325T020326 \r\n\n";
$message .= "DESCRIPTION: Please take one advil \r\n\n";
$message .= "Reminder - Medication \r\n\n";
$message .= "ORGANIZER; CN=\"Corporate\":mailto:mypharmacist@domain.com\r\n\n";
$message .= "Location:" . $location . "\r\n\n";
$message .= "UID:040000008200E00074C5B7101A82E00800000006FC30E6 C39DC004CA782E0C002E01A81\r\n\n";
$message .= "SEQUENCE:0\r\n\n";
$message .= "DTSTAMP:".date('Ymd').'T'.date('His')."\r\n\n";
$message .= "END:VEVENT\r\n\n";
$message .= "END:VCALENDAR\r\n\n";
#$message .= $message;
//mail($to, $subject, $message, $headers)
if(mail($to, $subject, $message, $headers))
echo "mail sent !!";
else
echo "mail not sent !!";

?>