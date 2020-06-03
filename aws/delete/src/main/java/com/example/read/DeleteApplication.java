package com.example.read;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
@EnableDiscoveryClient
public class DeleteApplication {

	public static void main(String[] args) {
		SpringApplication.run(DeleteApplication.class, args);
	}

}
