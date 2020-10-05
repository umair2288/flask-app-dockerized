docker build -t mlservice .

docker run -d -p 56733:80 --name=mltest -v $PWD:/app mlservice     

sudo docker stop mlservice && sudo docker start mlservice