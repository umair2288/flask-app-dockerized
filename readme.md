docker build -t mlservice .

docker run -d -p 56733:80 --name=mltest -v E:\Lakna\Flask\mlservice:/app mlservice     