<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Ag&ecirc;ncia virtual 4.1 - MENSAGEM</title>
	<!--Scripts-->
	<script type="text/javascript" src="../js/jquery-1.4.4.min.js"></script>
	<script type="text/javascript" src="../js/jquery-1.4.1.js"></script>
	<script type="text/javascript">
		$(document).ready(function() {
			$("#cmdFechar").click(function(){
				$(window.location).attr('href', '');
				/*alert('teste1');*/
			});
			$('#cmdOk').click(function(){ $(window.location).attr('href', '../logout.php'); }); $('#cmdFechar2').click(function(){ $(window.location).attr('href', '../logout.php'); });		});
	</script>
	
	<!--links-->	
	<link rel="stylesheet" href="../css/style.css" type="text/css">
</head>

<body class="fundoPrincipal">	
	<div align="center">
		<table width="100%">
		<tr height="150px"><td>&nbsp;</td></tr>
		<tr height="400px"><td align="center" valign="middle">
		<table width="40%" cellspacing="0" border="0" class="bordaMensagemErro">
			<tr bgcolor="#F3A8A8">
				<td align="left" valign="middle"><b><span style="font-family:Arial, Helvetica, sans-serif; font-size:14px; color:#FFFFFF;">&nbsp;Ag&ecirc;ncia virtual 5.0 - Erro</span></b></td>
				<td width="3%" align="right" valign="middle"><a href="#"><img src="../imagens/icon_close.png" border="0" height="20px" width="20px" name="cmdFechar2" id="cmdFechar2" /></a></td>
			</tr>
			<tr>
			  <td colspan="2">
			  	<table width="100%" cellspacing="0" sytle="border:2px solid #FFFFFF;">
					<tr bgcolor="#FFFFFF">
						<td width="25%" align="left" valign="middle"><img src='../imagens/icon_error.png' width='60px' height='60px' border='0' /></td>
						<td width="75%" align="center"><span style="font-family:Arial, Helvetica, sans-serif; font-size:16px; color:#000000;"> Identificador inv&aacute;lido. Verifique!</span></td>
					</tr>
				</table>			
			</td>
		  </tr>
			<tr bgcolor="#F3F3F3">			
			  <td colspan="2" align="right" valign="middle" height="35px"><button id='cmdOk'>&nbsp;&nbsp;&nbsp;OK&nbsp;&nbsp;&nbsp;</button></td>
		  </tr>
		</table>
		</td></tr></table>
	</div>
	<div id="rodape" class="divRodape">
		<table width="100%" border="0" cellspacing="0">
			<tr>
				<td width="30%" align="left" valign="bottom"><span class="textoVersao">Ag&ecirc;ncia virtual<br />
					Vers&atilde;o 4.1</span></td>
				
				
			</tr>
		</table>
	</div>
</body>
</html>
