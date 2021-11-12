# Exercise 3

## Requirements

Note: Please read all requirements before proceeding.

1. Using test-driven development techniques (as much as possible), implement new functionality in the rates app server to read its configuration from a YAML file. The YAML file should have the following structure:

```yaml
rates_api_server: http://127.0.0.1:5000
rates_app_server:
    host: 127.0.0.1
    port: 5050
```

The `rates_api_server` should be used in place of the hard coded string in the current version. The `rates_app_server` configuration should be used for the server socket.

To read YAML files, install the `pyyaml` package.

```python
with open(config_file_path) as yaml_file:
    config = yaml.load(yaml_file, Loader=yaml.SafeLoader)
```

2. The code that reads the configuration should be placed in a function named `read_config` and it should return a named tuple with the values. The `read_config` function should be unit tested.

3. Do not unit test the existing code that uses the new configuration.

4. If you attempt a test-driven approach, the order of tasks would look like this:

- Write a test for `read_config`
- Implement `read_config`
- Utilize `read_config` throughout the existing program

5. Ensure all tests pass and the code works.