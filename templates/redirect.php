<!DOCTYPE html>
<html>
<head>
<title>Agência virtual 4.1 - MENSAGEM</title>
	<script type="text/javascript" src="/static/js/jquery-1.4.4.min.js"></script>
	<script type="text/javascript" src="/static/js/jquery-1.4.1.js"></script>
	<script type="text/javascript">
		$(document).ready(function() {
			$("#cmdFechar").click(function(){
				$(window.location).attr('href', '');
			});
      $('#cmdOk').click(function(){ $(window.location).attr('href', '/');});
      $('#cmdFechar2').click(function(){ $(window.location).attr('href', '/');});
    });
	</script>
	<link rel="stylesheet" href="/static/css/style.css" type="text/css">
</head>

<body class="fundoPrincipal">	
	<div align="center">
		<table width="100%">
		<tr height="150px"><td></td></tr>
		<tr height="400px"><td align="center" valign="middle">
		<table width="40%" cellspacing="0" border="0" class="bordaMensagemErro">
			<tr bgcolor="#F3A8A8">
        <td align="left" valign="middle">
          <b><span style="font-family:Arial, Helvetica, sans-serif; font-size:14px; color:#FFFFFF;">Agência virtual 5.0 - Erro</span></b>
        </td>
				<td width="3%" align="right" valign="middle"><a href="#"><img src="/static/imagens/icon_close.png" border="0" height="20px" width="20px" name="cmdFechar2" id="cmdFechar2" /></a></td>
			</tr>
			<tr>
			  <td colspan="2">
			  	<table width="100%" cellspacing="0" sytle="border:2px solid #FFFFFF;">
					<tr bgcolor="#FFFFFF">
            <td width="25%" align="left" valign="middle">
              <img src='/static/imagens/icon_error.png' width='60px' height='60px' border='0'/>
            </td>
            <td width="75%" align="center">
              <span style="font-family:Arial, Helvetica, sans-serif; font-size:16px; color:#000000;">Identificador inválido. Verifique!</span>
            </td>
					</tr>
				</table>			
			</td>
		  </tr>
			<tr bgcolor="#F3F3F3">			
        <td colspan="2" align="right" valign="middle" height="35px">
          <button id='cmdOk'>OK</button>
        </td>
		  </tr>
		</table>
		</td></tr></table>
	</div>
	<div id="rodape" class="divRodape">
		<table width="100%" border="0" cellspacing="0">
			<tr>
        <td width="30%" align="left" valign="bottom">
          <span class="textoVersao">
            Agência virtual
            <br/>
            Versão 4.1
          </span>
        </td>
			</tr>
		</table>
	</div>
</body>
</html>
