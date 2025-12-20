echo "Script to Identify active network interface, assigned IPv4 adr and default gateway"

cat /proc/net/route > route.txt

ifc=$(awk -F' ' '$2==00000000,$7==100 {print$1}' route.txt)
ip=$(awk '$1=="enp0s3" {print$3}' ip1.txt)
gw=$(awk -F' ' '$2==00000000 {print$3}' route.txt)
#echo "$ifc"
#echo "$ip"
#echo "$gw"
echo "Interface: $ifc | IP: $ip | Gateway: $gw "