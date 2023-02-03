Get-Service
Get-Service "sql*"
Get-Service "sql*" Get-Member
Get-Help

New-Alias
New-Alias -Name gh -Value Get-Help

Get-Alias

#operators
$a = 10 #use '$' for declaring variable
$b = 30

$a+$b

#comparison operators
$a -lt $b #lessthan
$a -le $b #less than or equal
$a -eq $b #equal
$a -ne $b #not equal
$a -ge $b #greater than or equal

#logical op
$a -AND $b 
$a -OR $b
-NOT($a -AND $b)

#like op
$str1 = "contoso"
$str2 = "fabrikum"
$str1 -like "*kum" #ending with kum or not
$str1 -notlike "*kum"
$str1 -match "[m$]"
$str1 -notmatch "[k$]"
$str2 -like "fab*" #start with fab or not

#redirectional op
echo "this is powershell" > newfile.txt