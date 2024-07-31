format:
	@echo "Starting autoflake format"
	autoflake --recursive api apps configuration
	@echo "Starting isort format..."
	isort api apps configuration --skip __init__.py
	@echo "Starting black format..."
	black api apps configuration
	@echo "Starting pylint "
	pylint api apps configuration

test:
	@echo "Starting tests..."
	python manage.py test
