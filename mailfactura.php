<?php

// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
// Load Composer's autoloader
require 'vendor/autoload.php';
// Instantiation and passing `true` enables exceptions

if(!empty($_POST['nombre'] && $_POST['email'] && $_POST['mensaje'])){





$mail = new PHPMailer(true);
try {
    //Server settings
    $mail->SMTPDebug = 2;                                       // Enable verbose debug output
    $mail->isSMTP();                                            // Set mailer to use SMTP
    $mail->Host       = 'smtp.gmail.com';  // Specify main and backup SMTP servers
    $mail->SMTPAuth   = true;                                   // Enable SMTP authentication
    $mail->Username   = 'newpowerexperience2016@gmail.com';                     // SMTP username
    $mail->Password   = 'powerandmovie2016';                               // SMTP password
    $mail->SMTPSecure = 'tls';                                  // Enable TLS encryption, `ssl` also accepted
    $mail->Port       = 587;                                    // TCP port to connect to
    //Recipients
    $mail->setFrom($_POST['email']);
    $mail->addAddress($_POST['email'], 'MAtSTark');     // Add a recipient
    //$mail->addAddress('ellen@example.com');               // Name is optional
    $mail->addReplyTo($_POST['email'], 'SE HA ENVIADO CORRECTAMENTE EL MENSAJE');
    //$mail->addCC('cc@example.com');
    //$mail->addBCC('bcc@example.com');
    // Attachments
    //$mail->addAttachment('/var/tmp/file.tar.gz');         // Add attachments
    //$mail->addAttachment('/tmp/image.jpg', 'new.jpg');    // Optional name
    // Content
    $mail->isHTML(true);                                  // Set email format to HTML
    $mail->Subject = 'Tema del mensaje';
    $mail->Body    =  $_POST['mensaje']; 
    // echo<pre>
    // enviado desde: $_POST[email];
    // nombre: $_POST[nombre]; 
    // mensaje: $_POST[mensaje];  
    // echo</pre>";
   
    $mail->AltBody = $_POST['mensaje'];
    $mail->send();
    echo 'El mensaje ha sido enviado correctamente';
} catch (Exception $e) {
    echo "Error!!!: {$mail->ErrorInfo}";
}




}

?>