CODE_PATH = src/customer_success_balancing.py
IMAGE_NAME = rd-tech-challenge
TEST_PATH = tests.test_customer_success_balacing.TestCustomerSuccessBalancing

.PHONY : build
build :
	docker build --tag ${IMAGE_NAME} .

.PHONY : run
run :
	docker run --rm ${IMAGE_NAME} python3 ${CODE_PATH} ${args}

.PHONY : test
test :
	docker run --rm ${IMAGE_NAME} python3 -m unittest ${TEST_PATH}
