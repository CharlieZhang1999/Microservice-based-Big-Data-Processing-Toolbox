resource "google_container_cluster" "main_gke_cluster" {
    name     = var.cluster_name
    location = var.region
    remove_default_node_pool = true
    initial_node_count       = 1
    deletion_protection      = false

    workload_identity_config {
        workload_pool = "${var.project_id}.svc.id.goog"
    }
}


resource "google_container_node_pool" "main_node_pool" {
    name       = var.node_pool
    location   = var.region
    cluster    = google_container_cluster.main_gke_cluster.self_link
    node_count = 1

    node_config {
        preemptible  = false
        machine_type = var.machine_type
        disk_size_gb = 150
        # local_ssd_count = 1
    }
    
}

resource "null_resource" "deploy_services" {
    depends_on = [
        google_container_node_pool.main_node_pool
    ]
    
    provisioner "local-exec" {
        command = "gcloud container clusters get-credentials ${google_container_cluster.main_gke_cluster.name} --region=${google_container_cluster.main_gke_cluster.location}"
    }

    provisioner "local-exec" {
        command = "kubectl apply -f ./scripts/frontend-deployment.yaml"
    }

    provisioner "local-exec" {
        command = "kubectl apply -f ./scripts/frontend-lb.yaml"
    }

    provisioner "local-exec" {
        command = "kubectl apply -f ./scripts/jupyter-deployment.yaml"
    }

    provisioner "local-exec" {
        command = "kubectl apply -f ./scripts/jupyter-lb.yaml"
    }

    provisioner "local-exec" {
        command = "kubectl apply -f ./scripts/jenkins-deployment.yaml"
    }

    provisioner "local-exec" {
        command = "kubectl apply -f ./scripts/jenkins-lb.yaml"
    }

    provisioner "local-exec" {
        command = "kubectl apply -f ./scripts/sonarqube-deployment.yaml"
    }

    provisioner "local-exec" {
        command = "kubectl apply -f ./scripts/sonarqube-lb.yaml"
    }

    provisioner "local-exec" {
        command = "kubectl get services"
    }
}